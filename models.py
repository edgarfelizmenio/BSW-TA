from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import db_session, Base, engine

from crypto_config import *

class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key = True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    attributes = relationship("Attribute")

class Attribute(Base):
    __tablename__ = 'Attribute'
    attribute_id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    value = Column(String(50))

Base.metadata.create_all(engine)
db_session.commit()

def get_master_key():
    return {
        'pk': pk_string,
        'mk': mk_string
    }

def get_one_time_key(user_id):
    result = db_session.query(User).filter(User.user_id == user_id).first()
    if result is None:
        return None
    else:
        private_key = generate_key(result, [a.value for a in result.attributes])
        return {
            'user_id': user_id,
            'private_key': private_key
        }

def add_user(data):
    if 'first_name' not in data and 'last_name' not in data:
        return None
    user = User(
        first_name = data['first_name'],
        last_name = data['last_name']
    )
    db_session.add(user)
    db_session.flush()

    for a in data['attributes']:
        attribute = Attribute(
            user_id = user.user_id,
            value = a
        )
        db_session.add(attribute)
    db_session.commit()

    private_key = generate_key(user, data['attributes'])

    return {
        'user_id': user.user_id,
        'private_key': private_key
    }

def get_user(user_id):
    result = db_session.query(User).filter(User.user_id == user_id).first()
    if result is None:
        return None
    else:
        user_object = {
            'user_id': result.user_id,
            'first_name': result.first_name,
            'last_name': result.last_name
        }
        attributes = []
        for attribute_result in result.attributes:
            attributes.append(attribute_result.value)
        user_object['attributes'] = attributes
    return user_object

def update_user(user_id, data):
    result = db_session.query(User).filter(
        User.user_id == user_id).first()
    if result is None:
        return None
    else:
        result.first_name = data.get('first_name', result.first_name)
        result.last_name = data.get('last_name', result.last_name)
        db_session.flush()
        
        # delete all existing attributes
        attribute_results = db_session.query(Attribute).filter(
            Attribute.user_id == user_id
        ).all()
        for attribute_result in result.attributes:
            db_session.delete(attribute_result)
        db_session.flush()

        # insert new attributes
        for a in data['attributes']:
            attribute = Attribute(
                user_id = user_id,
                value = a
            )
            db_session.add(attribute)
        db_session.commit()
    private_key = generate_key(result, data['attributes'])
    return {
        'user_id': result.user_id,
        'private_key': private_key
     }

def generate_key(user, attributes):
    attribute_set = [str(user.user_id), user.first_name, user.last_name] + attributes
    secret_key = hybrid_abe.keygen(pk, mk, attribute_set)
    sk_bytes = objectToBytes(secret_key, group_object)
    return str(sk_bytes, 'utf-8')

# for test purposes
def clear_tables():
    attributes = db_session.query(Attribute).all()
    users = db_session.query(User).all()
    for attribute in attributes:
        db_session.delete(attribute)
    for user in users:
        db_session.delete(user)
    db_session.commit()