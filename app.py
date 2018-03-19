from flask import Flask
from flask_restful import Api
import config

app=Flask(__name__)
api = Api(app)

import database

@app.teardown_appcontext
def shutdown_session(Exception = None):
    database.db_session.remove()

import resources

api.add_resource(resources.MasterKey, '/masterkey')
api.add_resource(resources.User, '/user/<int:user_id>')
api.add_resource(resources.AddUser, '/user')
api.add_resource(resources.OneTimeKey, '/user/<int:user_id>/sk')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)