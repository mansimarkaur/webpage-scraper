from flask_mongoalchemy import MongoAlchemy, BaseQuery
from flask import Flask
 
crawler =  Flask(__name__)
crawler.config['MONGOALCHEMY_DATABASE'] = 'websites'
db = MongoAlchemy(crawler)

class URL_db (db.Document) :
	query_class = getURL_db
	sites = db.StringField()
	images = db.ListField(db.Field())
	links = db.ListField(db.Field())
	text = db.StringField()
	indent = db.StringField()

class getURL_db(db.Document) :
	def getHyperlinks(self) :
		return self.filter(self.type.sites)


