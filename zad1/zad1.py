from flask import Flask

app = Flask(__name__)

@app.route("/")
def empty_string():
	return ""

@app.route("/<string:input_text>")
def reverse_string(input_text):
    return input_text[::-1]