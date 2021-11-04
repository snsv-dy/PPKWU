from flask import Flask
import os
# from flask import request

app = Flask(__name__)

print(f'Remote api url: {os.environ["API_URL"]}')

@app.route("/test_string/<string:format>/<string:input_text>", methods=['get'])
def test_string(format, input_text):

	return f"{format}, {input_text}"