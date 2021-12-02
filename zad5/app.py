from flask import Flask, Response, request
import os
import requests
from bs4 import BeautifulSoup
import re
# from flask import request

app = Flask(__name__)

content_types = {
	"txt": "text/plain; charset=UTF-8",
	"json": "application/json",
	"xml": "text/xml",
	"csv": "text/csv; charset=UTF-8",
	None: "text/plain; charset=UTF-8"
}

regexes = {
	"json": r"\"rodzaj_znakow\"\:\s\"(\d+)\"",
	"txt": r"Rodzaj znaków\:\s(\d+)\.",
	"xml": r"\<rodzaj_znakow\>(\d+)\<\/rodzaj_znakow\>",
	"csv": r"\"Rodzaj znaków\"\n(\d+)"
}

api_url = "http://panoramafirm.pl/szkoła"

@app.route("/query/<string:query_string>", methods=["get"])
def aba(query_string):
	result = requests.get(api_url)
	
	soup = BeautifulSoup(result.text, 'html.parser')
	company_list = soup.find(id="company-list")

	ret = "<ul>"
	for elem in company_list.children:
		title = elem.find_next(class_="company-name")
		if title is not None:
			title = title.get_text()
		t = f"<li><a href=\"/vcard\">Generuj vcard</a>Nazwa firmy: {title}</li>"
		ret += t 

	ret += "</ul>"

	return ret
	