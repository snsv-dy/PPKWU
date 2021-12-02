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

api_url = "http://panoramafirm.pl/"

# def genVcard(name, address, phone, email):
	

@app.route("/vcard/<name>/<address>/<phone>/<email>", methods=["get"])
def vc(name, address, phone, email):
	card = f'''BEGIN:VCARD
VERSION:2.1
FN:Imie Nazwisko
N:{name}
ADR;WORK;PREF;ENCODING=QUOTED-PRINTABLE:;{address}
TEL;CELL:{phone}
EMAIL;INTERNET:{email}
UID:
END:VCARD'''

	resp = Response(card)
	resp.headers['Content-Type'] = content_types.get('text/vcard')
	return resp

@app.route("/query/<string:query_string>", methods=["get"])
def aba(query_string):
	result = requests.get(api_url + query_string)
	
	soup = BeautifulSoup(result.text, 'html.parser')
	company_list = soup.find(id="company-list")

	ret = "<ul>"
	for elem in company_list.children:
		try:
			title = elem.find_next(class_="company-name")
			phone = elem.find_next(class_="icon-telephone").get('title')
			email = elem.find_next(class_="icon-envelope").get('data-company-email')
			addr = elem.find_next(class_="address").contents[-1]
			print("title: ", title)
			print("phone: ", addr)
			# print("title: ", title)
			if title is not None:
				title = title.get_text()
			t = f"<li><a href=\"/vcard/{title}/{addr}/{phone}/{email}\">Generuj vcard</a>Nazwa firmy: {title}, telefon: {phone}, email: {email}, address: {addr}</li>"
			ret += t 
		except:
			pass

	ret += "</ul>"

	return ret
	