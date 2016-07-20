# webpage-scraper
`webpage-scraper` is a *flask* based application which allows the users to :

- Input URL with the freedom of inputting it with/ without the protocol and sub-domain specifiers.
- Fetch a list of URLs to all the images on the webpage with an option to download all the images in a directory with name specified by the user.
- Get a list of all the hyperlinks on the webpage. Save them into a text file with a name specified by the user.
- Get the indented html source code of the webpage  and save it in a .html file with a user-provided name.
- Fetch the text on the webpage stripping the html code. Save it in a text file with a filename of user's choice.
- The database is deployed on [mLab](http://mlab.com/) and uses *MongoDB* for fast access to long list of images, hyperlinks and text for a URL that has been requested by some other user in the past, thus, reducing processing time for subsequent users.

## Pre- requisites
 See [requirements] (https://github.com/mansimarkaur/webpage-scraper/blob/master/requirements.txt)
	 
To install flask:

	```
	[sudo] pip install flask
	```
	 	
	If you don't have [pip](https://pip.pypa.io) installed, [this Python installation guide](http://docs.python-guide.org/en/latest/starting/installation) can guide you through the process.

	
To install BeautifulSoup:

	```
	[sudo] pip install bs4
	```
		 	
	OR
	
	[download the Beautiful Soup 4 source tarball](https://www.crummy.com/software/BeautifulSoup/bs4/download/4.0/) and install it with `setup.py`
	
	`python setup.py install`
	
To install requests:

	```
	[sudo] pip install requests
	```
	 	
	OR
	
	`git clone git://github.com/kennethreitz/requests.git` 
	
	OR
	
	download the [tarball](https://github.com/kennethreitz/requests/tarball/master)
	
	```
	curl -OL https://github.com/kennethreitz/requests/tarball/master
	#optionally, zipball is also available (for Windows users).
	```
		 	
	`python setup.py install`
	
To install MongoDB Community Edition:

	- on OSX, refer to:
		https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/

	- on Ubuntu, refer to:
		https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

	- on Windows, refer to:
		https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
	
To install flask_mongoalchemy:

	```
	[sudo] pip install flask-mongoalchemy
	```
		 	
	OR
	
	```
	git clone https://github.com/cobrateam/flask-mongoalchemy.git
	cd flask-mongoalchemy
	[sudo] python setup.py develop
	```
	
**Make sure you have MongoDB installed**

## Getting started
```	
git clone http://github.com/mansimarkaur/webpage-scraper 
cd webpage-scraper
python crawler_flask.py
```

Open **http://127.0.0.1:5000/** in your browser.
Input URL and **have fun** :+1:
	

	
