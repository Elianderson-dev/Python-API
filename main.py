# Import the necessary libraries

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine("sqlite:///test.db")
app = Flask(__name__)
api - Api(app)


