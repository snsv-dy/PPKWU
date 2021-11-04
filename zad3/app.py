from flask import Flask, Response
import os
import requests
# from flask import request

app = Flask(__name__)

print(f'Remote api url: {os.environ["API_URL"]}')

content_types = {
	"txt": "text/plain",
	"json": "application/json"
}

def format_result(format, value):
	
	if format == 'txt':
		result = f"Rodzaj znaków: {value}."
	elif format == 'json':
		result = "{ \"rodzaj_znakow\": " + value + " }"
	else:
		raise Exception()
	
	resp = Response(result)
	resp.headers['Content-Type'] = content_types[format]

	return resp

@app.route("/test_string/<string:format>/<string:input_text>", methods=['get'])
def test_string(format, input_text):
	try:
		api_response = requests.get(os.environ["API_URL"] + "/test_string/" + input_text)
		result = format_result(format, api_response.text)
		print("after result")
		return result
	except:
		print("expected")
		pass
	return ""
	# return f"{format}, {input_text}"