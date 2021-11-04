from flask import Flask
# from flask import request

app = Flask(__name__)

@app.route("/", methods=['get'])
def test_string(input_text):
	return ""