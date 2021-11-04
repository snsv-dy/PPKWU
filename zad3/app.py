from flask import Flask, Response
import os
import requests
# from flask import request

app = Flask(__name__)

print(f'Remote api url: {os.environ["API_URL"]}')

content_types = {
	"txt": "text/plain; charset=UTF-8",
	"json": "application/json",
	"xml": "text/xml",
	"csv": "text/csv; charset=UTF-8",
	None: "text/plain; charset=UTF-8"
}

def format_result(format, value):
	
	if format == 'txt':
		result = f"Rodzaj znaków: {value}."
	elif format == 'json':
		result = "{ \"rodzaj_znakow\": " + value + " }"
	elif format == 'xml':
		result = f"""<?xml version="1.0" encoding="UTF-8"?>
<rodzaj_znakow>{value}</rodzaj_znakow>
		"""
	elif format == 'csv':
		result = f"""\"Rodzaj znaków\"
{value}
		"""
	else:
		result = ""
	
	resp = Response(result)
	resp.headers['Content-Type'] = content_types.get(format)

	return resp

@app.route("/test_string/<string:format>/<string:input_text>", methods=['get'])
def test_string(format, input_text):
	try:
		api_response = requests.get(os.environ["API_URL"] + "/test_string/" + input_text)
		result = format_result(format, api_response.text)
		return result
	except:
		pass
	return ""
	# return f"{format}, {input_text}"