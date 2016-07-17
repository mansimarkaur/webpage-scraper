import urllib2
import urllib
import os
import sys
from flask import Flask, flash, request, render_template
from bs4 import BeautifulSoup
from flask_mongoalchemy import MongoAlchemy

crawler = Flask(__name__)
crawler.secret_key = 'I <3 physics'
# crawler.config['MONGOALCHEMY_DATABASE'] = 'website'
# db = MongoAlchemy(crawler)

from model import db

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
		"text" : text,
		"formatter" : formatter
		}
	func = dict.get(job) #calls function acc to button pressed
	return func()


#displays image URLs
@crawler.route("/download_images", methods = ['POST'])
def image() :
	img = soup.find_all("img") #finds all <img>
	if len(img) == 0 :
		return render_template("index.html", text = ["No images to fetch"])
	images =[]
	for i in img :
		images.append(url + i.get("src")) #adds src attribute value to images list
		images_db(site = URL_db(website = url), img = images[-1]).save()
	try :
		to_download = bool(request.form['submit'])
		dir_name = request.form['name']
	except :
		to_download = False
	if to_download :
		download(images, dir_name)
		flash('Download completed')
	return render_template("images.html", text = images)


def download(image, dir_name) :
	try :
		os.stat(dir_name)
	except :
		os.mkdir(dir_name)
	for i in image :
		name = i[i.rfind("/")+1:]
		if name == -1 :
			name = i
		print dir_name+'/'+name
		urllib.urlretrieve(i, dir_name+'/'+name)

#displays hyperlinks
@crawler.route('/download_links', methods = ['POST'])
def hyperlinks() :
	URL_db.query.getHyperlinks().first()
	link = soup.find_all("a") #finds all <a>
	if len(link) == 0 :
		return render_template("index.html", text = ["No links to fetch"])
	links = []
	for i in link :
		l = i.get("href") #adds href attribute value to links list
		if l[:4] != "http" :
			l = url + l 
		links.append(l)
	URL_db.query.getHyperlinks().first()
	URL_db(sites = url, link = l).save()
	try :
		to_download = bool(request.form['submit'])
		file_name = request.form['name']
	except :
		to_download = False
	if to_download :
		with open(file_name + ".txt", "w+") as getlink :
			for i in links :
				getlink.write(i)
		flash('Download completed')
	return render_template("links.html", text = links)

#displays text after stripping html tags from src code
@crawler.route('/text', methods = ['POST'])
def text() :
	t = soup.get_text()#.encode('UTF-8') 
	text_db(site = URL_db(website = url), txt = t).save()
	try :
		to_download = bool(request.form['submit'])
		file_name = request.form['name']
	except :
		to_download = False
	if to_download :
		with open(file_name + ".txt", "w+") as pretty :
			pretty.write(t.encode('UTF-8'))
		flash('Download completed')
	return render_template("text.html", text = t)

#displays formatted html src code
@crawler.route('/download_code', methods = ['POST'])
def formatter() :
	code = soup.prettify()#.encode('UTF-8')
	indent_db(site = URL_db(website = url), format = code).save()
	try :
		to_download = bool(request.form['submit'])
		file_name = request.form['name']
	except :
		to_download = False
	if to_download :
		with open(file_name + ".html", "w+") as source_code :
			source_code.write(code.encode('UTF-8'))
		flash('Download completed')
	return render_template("indent.html", text = code)

# class url (db.document) :
# 	name = db.StringField()

# class images (db.document) :
# 	url = db.DocumentField(url)
# 	img = db.StringField()

# class hyperlinks (db.document) :
# 	url = db.DocumentField(url)
# 	link = db.StringField()

# class text (db.document) :
# 	url = db.DocumentField(url)
# 	txt = db.StringField()

# class indent (db.document) :
# 	url = db.DocumentField(url)
# 	format = db.StringField()

if __name__ == "__main__" :
	crawler.run()

