from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def empty_string(methods=['get','post','put','delete','update']):
	return "0"

@app.route("test_string/<string:input_text>", methods=['get','post','put','delete','update'])
def test_string(input_text):
    return 