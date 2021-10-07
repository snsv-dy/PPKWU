from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def empty_string():
	return str(request.data)[::-1] 

# @app.route("/<string:input_text>")
# def reverse_string(input_text):
#     return input_text[::-1]