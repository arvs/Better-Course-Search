from flask import Flask, render_template, url_for, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	r = requests.get('http://culpa.info/gold_nuggets')
	page = BeautifulSoup(r.content)
	names = filter(lambda x: u'(TA)' not in x, [list(x.parent.children)[0].contents[0].split(u'\xa0') for x in page.find_all("img", "nugget")])
	profs = []
	for name in names:
		name = "%s %s" % (name[1].strip(','), name[0].strip(','))
		profs.append(name)

	return render_template('index.html', profs=profs, js_url=url_for("static",filename="search_cu.js"))

@app.route('/search_for_prof')
def search_for_prof():
	name = request.args.get("name","")
	params = {"q" : name, 
			  "site" : "Directory_of_Classes", 
			  "num" : 20, 
			  "filter" : 0,
			  "entqr" : 0, 
			  "ud" : 1,
			  "sort" : "date%3AD%3AL%3Ad1", 
			  "output" : "xml_no_dtd",
			  "oe" : "UTF-8",
			  "ie" : "UTF-8",
			  "client" : "DoC",
			  "proxystylesheet" : "DoC",
			  "proxyreload" : 1}
	search = requests.get("http://search.columbia.edu/search", params=params)
	search_result = BeautifulSoup(search.content)
	if search_result.find(id="empty") is None:
		classes = []
		for cls in search_result.find_all("a","l"):
			if "Fall 2012" in "".join(map(str, cls.contents)):
				classes.append(cls.get('href'))
		return jsonify(name=name, classes=classes)

	return jsonify(name=name, classes=[])

if __name__ == '__main__':
	app.run()