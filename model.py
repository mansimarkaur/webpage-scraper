from flask_mongoalchemy import MongoAlchemy, BaseQuery
from flask import Flask
 
crawler =  Flask(__name__)
crawler.secret_key = 'continents9794'
crawler.config['MONGOALCHEMY_DATABASE'] = 'website-scraper'
crawler.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://scraper:continents@ds023495.mlab.com:23495/website-scraper'

db = MongoAlchemy(crawler)

class db_query(BaseQuery) :
	def text_query(self, url) :
		return self.filter(self.type.sites == url).fields('text')

	def images_query(self, url) :
		return self.filter(self.type.sites == url).fields('images')

	def links_query(self, url) :
		return self.filter(self.type.sites == url).fields('links')

	def indent_query(self, url) :
		return self.filter(self.type.sites == url).fields('indent')

class images_db(db.Document) :
	query_class = db_query
	sites       = db.StringField()
	images      = db.ListField(db.StringField())

class links_db(db.Document) :
	query_class = db_query
	sites       = db.StringField()
	links       = db.ListField(db.StringField())

class indent_db(db.Document) :
	query_class = db_query
	sites       = db.StringField()
	indent      = db.StringField()

class text_db(db.Document) :
	query_class = db_query 
	sites       = db.StringField()
	text        = db.StringField()



