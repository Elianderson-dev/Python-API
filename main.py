# Import the necessary libraries

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine("sqlite:///test.db")
app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from user")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        name = request.json["name"]
        email = request.json["email"]

        conn.execute(
                "insert into user values(null, '{0}', '{1}')".format(name, email)
                )

        query = conn.execute("select * from user by id desc limit 1")
        result = [disc(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    
