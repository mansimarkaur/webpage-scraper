from flask_mongoalchemy import MongoAlchemy, BaseQuery
from flask import Flask
 
crawler =  Flask(__name__)
crawler.config['MONGOALCHEMY_DATABASE'] = 'website-scraper'
crawler.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://scraper:continents@ds023495.mlab.com:23495/website-scraper'

db = MongoAlchemy(crawler)

# class getURL_db(BaseQuery) :
# 	def getInfo(self, info, url) :
# 		return self.filter(self.type.info == url)


class images_db(db.Document) :
	sites = db.StringField()
	images = db.ListField(db.StringField())

class links_db(db.Document) :
	sites = db.StringField()
	links = db.ListField(db.StringField())

class indent_db(db.Document) :
	sites = db.StringField()
	indent = db.StringField()

class text_db(db.Document) :
	sites = db.StringField()
	text = db.StringField()



