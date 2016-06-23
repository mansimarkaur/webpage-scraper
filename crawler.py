import urllib2
import urllib
import os
import sys
from flask import Flask
from bs4 import BeautifulSoup

scrape = Flask(__name__)

@crawler.route("/")
def main() :
	return render_template("index.html")

url = raw_input("Enter URL")
if not (url.startswith("http://") or url.startswith("https://"))  :
	url = "http://" + url
if not url.endswith("/") :
	url = url + "/"
link = urllib2.urlopen(url)
soup = BeautifulSoup(link, 'html.parser')

# def menu():
# 	print "Choose and enter corresponding index of option"
# 	print "1. Fetch images"
# 	print "2. Fetch hyperlinks"
# 	print "3. Fetch text"
# 	print "4. Format HTML"
# 	print "5. Exit"
# 	option = raw_input()
# 	return option 


##hook function
def hook(count_transferred, block_size, total_size) :
	tot = int(total_size/block_size)
	for i in range(count_transferred) :
		print "#",
	for i in range(tot - count_transferred):
		print "_",
	print "|" + "%s % downloaded"%(count_transferred*100/tot)



##download
def download(img) :
	dir_name = url[7:] 
	print url + img
	print dir_name+img
	try :
		os.stat(dir_name)
	except :
		os.mkdir(dir_name)
	urllib.urlretrieve(url+img, dir_name+img, hook)

##images
@crawler.route("#image")
def image() :
	img = soup.find_all("img")
	if len(img) == 0 :
		print "No images to fetch"
		return
	for i in img :
		download(i.get("src"))
		print i.get("src")


##links
@crawler.route("#hyperlinks")
def hyperlinks() :
	img = soup.find_all("a")
	if len(img) == 0 :
		print "No hyperlinks to fetch"
		return
	for i in img :
		print i.get("href")

##text
@crawler.route("#text")
def text() :
	print soup.get_text().encode('UTF-8')

##formatter
@crawler.route("#formatter")
def formatter() :
	yes = raw_input("Do you want to save the formatted html in a .html file? Press Y for yes and any other key for no.")
	yes = yes.upper()
	if yes == "Y" :
		name = raw_input("Enter name of file")
		with open(name+".html","w+") as pretty :
			pretty.write(soup.prettify().encode('UTF-8'))
		print "Updated contents of file"
	else :
		print soup.prettify().encode('UTF-8')
	
# @crawler.route("#exit")
# def exit_scraper() :
# 	sys.exit("Bye :)")

# def main(option) :

# 	dict = {
# 		"1" : image,
# 		"2" : hyperlinks,
# 		"3" : text,
# 		"4" : formatter,
# 		"5" : exit_scraper
# 	}

# 	for i in dict :
# 		if option == i :
# 			func = dict.get(option, lambda option : "%s is an invalid option."%option)
# 			print func
# 			return func()
# 	else :
# 		print "Enter valid option please!"
# 	main(menu())

if __name__ == "__main__" :
	crawler.run()