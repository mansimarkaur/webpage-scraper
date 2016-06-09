import urllib2
from bs4 import BeautifulSoup
url = raw_input("Enter URL")
link = urllib2.urlopen(url)
soup = BeautifulSoup(link, 'html.parser')

print "Choose and enter corresponding index of option"
print "1. Fetch images"
print "2. Fetch hyperlinks"
print "3. Fetch text"
print "4. Format HTML"
option = raw_input()


##images
def image() :
	img = soup.find_all("img")
	for i in img :
		print i.get("src")
##links
def hyperlinks() :
	img = soup.find_all("a")
	for i in img :
		print i.get("href")

##text
def text() :
	print soup.get_text().encode('UTF-8')

"""
##formatter
def format() :
	print soup.prettify()"""

	

def main(option) :

	dict = {
		"1" : image,
		"2" : hyperlinks,
		"3" : text,
	}
	func = dict.get(option, lambda : "Invalid")
	print func
	return func()

main(option)












