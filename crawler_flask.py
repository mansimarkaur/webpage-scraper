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
	url = request.form["inputName"] #fetches user entered URL
	if not(url.startswith("http://") or url.startswith("https://")) :
		url = "http://" + url
	if not url.endswith("/") :
		url = url + "/"
	print url
	link = urllib2.urlopen(url) #returns obj 
	soup = BeautifulSoup(link, 'html.parser') #returns beautifulsoup obj
	job = request.form["submit"]
	dict = {
		"images" : image,
		"hyperlinks" : hyperlinks,
		"text" : txt,
		"formatter" : formatter
		}
	func = dict.get(job) #calls function acc to button pressed
	return func(url, soup)

#displays image URLs
def image(url, soup) :
	img = soup.find_all("img") #finds all <img>
	if len(img) == 0 :
		return render_template("index.html", text = ["No images to fetch"])
	images =[]
	for i in img :
		images.append(url + i.get("src")) #adds src attribute value to images list
	return render_template("index.html", text = images)

#displays hyperlinks
def hyperlinks(url, soup) :
	link = soup.find_all("a") #finds all <a>
	if len(link) == 0 :
		return render_template("index.html", text = ["No links to fetch"])
	links = []
	for i in link :
		l = i.get("href") #adds href attribute value to links list
		if l[:4] != "http" :
			l = url + l 
		links.append(l)
	return render_template("index.html", text = links)

#displays text after stripping html tags from src code
def txt(url, soup) :
	t = soup.get_text()#.encode('UTF-8') 
	print type(t)
	return render_template("index.html", text = t)

#displays formatted html src code, (not sure how it'll behave in index.html after being rendered)
def formatter(url, soup) :
	code = soup.prettify().encode('UTF-8')
	return render_template("index.html", text = txt)

@crawler.route("/download") 
def download() :
	pass


if __name__ == "__main__" :
	crawler.run()

