from flask import request
from flask_restful import Resource

import models

class MasterKey(Resource):
    def get(self):
        key_object = models.get_master_key()
        return key_object, 200

class User(Resource):
    def get(self, user_id):
        user_object = models.get_user(user_id)
        if user_object is None:
            return {'status': 404, 'message': 'User with id={} not found.'.format(user_id)}
        return user_object, 200

    def put(self, user_id):
        data = request.get_json()
        result = models.update_user(user_id, data)
        if result is None:
            return {'status': 400, 'message': 'Insufficient Data'}
        return result, 200

class AddUser(Resource):
    def post(self):
        data = request.get_json()
        result = models.add_user(data)
        if result is None:
            return {'status': 400, 'message': 'Insufficient Data'}
        return result, 200

class OneTimeKey(Resource):
    def get(self, user_id):
        one_time_key = models.get_one_time_key(user_id)
        if one_time_key is None:
            return {'status': 404, 'message': 'User with id={} not found.'}
        return one_time_key, 200