from flask import Flask, Response, request
import os
import requests
import re
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

formats = ["txt", "json", "xml", "csv"]

def format_result(format, value):
	
	if format == 'txt':
		result = f"Rodzaj znaków: {value}."
	elif format == 'json':
		result = "{ \"rodzaj_znakow\": " + str(value) + " }"
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

regexes = {
	"json": r"\"rodzaj_znakow\"\:\s\"(\d+)\"",
	"txt": r"Rodzaj znaków\:\s(\d+)\.",
	"xml": r"\<rodzaj_znakow\>(\d+)\<\/rodzaj_znakow\>",
	"csv": r"\"Rodzaj znaków\"\n(\d+)"
}

@app.route("/convert_string/<string:source_format>/<string:dest_format>/<string:input_text>", methods=["get"])
def abab(source_format, dest_format, input_text):
	if source_format in formats and dest_format in formats:
		try:
			api_response = requests.get(os.environ["API_URL"] + "/test_string/" + source_format + "/" + input_text)
			parsed = re.findall(regexes[source_format], api_response.text)[0]
			result = format_result(dest_format, parsed)
			return result
		except Exception as ex:
			pass
	return ""

@app.route("/convert_string/<string:source_format>/<string:dest_format>", methods=["post"])
def aba(source_format, dest_format):
	if source_format in formats and dest_format in formats:
		data = request.data.decode("utf-8")
		parsed = re.findall(regexes[source_format], data)
		if len(parsed) > 0:
			result = format_result(dest_format, int(parsed[0]))
			return result
	return ""
