import urllib2
import urllib
import os
import sys
from flask import Flask, request, render_template
from bs4 import BeautifulSoup

crawler = Flask(__name__)


@crawler.route("/")
def main() :
	return render_template("index.html")

@crawler.route("/driver", methods = ['POST'])
def driver() :
	global url
	url = request.form["inputName"] #fetches user entered URL
	print url
	if not(url.startswith("http://") or url.startswith("https://")) :
		if not url.startswith("www.") :
			url = "www." + url
		url = "http://" + url
	if not url.endswith("/") :
		url = url + "/"
	print url
	link = urllib2.urlopen(url) #returns obj 
	global soup
	soup = BeautifulSoup(link, 'html.parser') #returns beautifulsoup obj
	job = request.form["submit"]
	dict = {
		"images" : image,
		"hyperlinks" : hyperlinks,
		"text" : txt,
		"formatter" : formatter
		}
	func = dict.get(job) #calls function acc to button pressed
	return func()


#displays image URLs
def image(to_download) :
	img = soup.find_all("img") #finds all <img>
	if len(img) == 0 :
		return render_template("index.html", text = ["No images to fetch"])
	images =[]
	for i in img :
		images.append(url + i.get("src")) #adds src attribute value to images list
		#if to_download :
			#download(url, i.get("src"))
	return render_template("images.html", text = images)

def download(image) :
	print url
	print image
	dir_name = url[7:]
	print dir_name+image
	print url+image
	try :
		os.stat("let")
	except :
		os.mkdir("let")
	urllib.urlretrieve(url+image, "let")

#displays hyperlinks
def hyperlinks() :
	link = soup.find_all("a") #finds all <a>
	if len(link) == 0 :
		return render_template("index.html", text = ["No links to fetch"])
	links = []
	for i in link :
		l = i.get("href") #adds href attribute value to links list
		if l[:4] != "http" :
			l = url + l 
		links.append(l)
	return render_template("links.html", text = links)

#displays text after stripping html tags from src code
def txt() :
	t = soup.get_text()#.encode('UTF-8') 
	return render_template("text.html", text = t)

#displays formatted html src code, (not sure how it'll behave in index.html after being rendered)
def formatter() :
	code = soup.prettify()#.encode('UTF-8')
	return render_template("indent.html", text = code)

#downloading functions

@crawler.route('/text', methods = ['POST'])
def text() :
	t = soup.get_text()#.encode('UTF-8') 
	try :
		to_download = bool(request.form['submit'])
		file_name = request.form['name']
	except :
		to_download = False
	if to_download :
		with open(file_name + ".txt", "w+") as pretty :
			pretty.write(t.encode('UTF-8'))
	return render_template("text.html", text = t)

@crawler.route('/download_links', methods = ['POST'])
def download_links() :
	link = soup.find_all("a")
	links = []
	for i in link :
		l = i.get("href") #adds href attribute value to links list
		if l[:4] != "http" :
			l = url + l 
		links.append(l)
	try :
		to_download = bool(request.form['submit'])
		file_name = request.form['name']
	except :
		to_download = False
	if to_download :
		with open(file_name + ".txt", "w+") as getlink :
			for i in links :
				getlink.write(i)
	return render_template("links.html", text = links)

@crawler.route('/download_code', methods = ['POST'])
def download_code() :
	code = soup.prettify()
	try :
		to_download = bool(request.form['submit'])
		file_name = request.form['name']
	except :
		to_download = False
	if to_download :
		with open(file_name + ".html", "w+") as source_code :
			source_code.write(code.encode('UTF-8'))
	return render_template("indent.html", text = code)




if __name__ == "__main__" :
	crawler.run()

