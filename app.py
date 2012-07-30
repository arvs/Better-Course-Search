from flask import Flask, render_template, Response, url_for, make_response, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
	r = requests.get('http://culpa.info/gold_nuggets')
	page = BeautifulSoup(r.content)
	return page.prettify()

if __name__ == '__main__':
	app.run()