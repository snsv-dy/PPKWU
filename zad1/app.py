from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def empty_string(methods=['get','post','put','delete','update']):
	return ""

@app.route("/<string:input_text>", methods=['get','post','put','delete','update'])
def reverse_string(input_text):
    return input_text[::-1]