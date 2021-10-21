from flask import Flask
from flask import request

TYPE_UPPERCASE	= 0x1
TYPE_LOWERCASE	= 0x2
TYPE_NUMBER		= 0x4
TYPE_SPECIAL	= 0x8

app = Flask(__name__)

@app.route("/test_string/<string:input_text>", methods=['get'])
def test_string(input_text):
	types = 0
	for c in input_text:
		if c.isupper():
			types |= TYPE_UPPERCASE
		elif c.islower():
			types |= TYPE_LOWERCASE
		elif c.isdigit():
			types |= TYPE_NUMBER
		elif not c.isspace() and c.isprintable():
			types |= TYPE_SPECIAL
			
	return str(types)