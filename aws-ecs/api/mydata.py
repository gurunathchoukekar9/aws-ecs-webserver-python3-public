# api/mydata.py

from flask import Blueprint, jsonify, request, make_response
from flask_restful import Api, Resource
from db.postgre_db import MyPostgreDb
from flask_expects_json import expects_json
import json
import os


mydata_blueprint = Blueprint("mydata", __name__)
api = Api(mydata_blueprint)


class MyData(Resource):

    def __init__(self):
        db_name = os.getenv('POSTGRE_DB_NAME')
        db_user = os.getenv('POSTGRE_DB_USER')
        db_password = os.getenv('POSTGRE_DB_PASSWORD')
        db_host = os.getenv('POSTGRE_DB_HOST')
        db_port = os.getenv('POSTGRE_DB_PORT', "5432")
        self.my_db = MyPostgreDb(
            db_name, db_user, db_password, db_host, db_port)

    def get(self):
        print(f"inside /mydata GET method")
        result = self.my_db.list_custom_data()
        print(f"Return from /mydata GET = {result}")
        dict = {
            'Records': result,
            'RecordsCount': len(result)
        }
        return jsonify(dict)

    @expects_json()
    def post(self):
        print(f"inside /mydata POST method")
        record = json.loads(request.data)
        result = self.my_db.insert_custom_data(record)
        print(f"Return from /mydata POST = {result}")
        message = None
        if result == None:
            message = {"status": "failure",
                       "message": "FAILED TO INSERT RECORD IN DATABASE",
                       "data": record}
            return make_response(jsonify(message), 500)
        else:
            message = {"status": "success",
                       "message": "Record inserted in database",
                       "data": record}
            return make_response(jsonify(message), 200)


api.add_resource(MyData, "/mydata")
