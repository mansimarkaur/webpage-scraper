import urllib2
import sys
from bs4 import BeautifulSoup
url = raw_input("Enter URL")
link = urllib2.urlopen(url)
soup = BeautifulSoup(link, 'html.parser')

def menu():
	print "Choose and enter corresponding index of option"
	print "1. Fetch images"
	print "2. Fetch hyperlinks"
	print "3. Fetch text"
	print "4. Format HTML"
	print "5. Exit"
	option = raw_input()
	return option 


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

##formatter
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
	

def exit_scraper() :
	sys.exit("Bye :)")

def main(option) :

	dict = {
		"1" : image,
		"2" : hyperlinks,
		"3" : text,
		"4" : formatter,
		"5" : exit_scraper
	}

	for i in dict :
		if option == i :
			func = dict.get(option, lambda option : "%s is an invalid option."%option)
			print func
			return func()
	else :
		print "Enter valid option please!"
	main(menu())

if __name__ == "__main__" :
	main(menu())