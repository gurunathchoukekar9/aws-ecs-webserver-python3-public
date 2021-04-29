# api/health.py

from flask import Blueprint,jsonify
from flask_restful import Api, Resource

health_blueprint = Blueprint("health", __name__)
api = Api(health_blueprint)


class Health(Resource):
    def get(self):
        message = {"status": "success",
                   "message": "Hello world !! from aws ecs service health check"}
        print(f"Return from /health is = {message}")
        return jsonify(message)


api.add_resource(Health, "/health")
