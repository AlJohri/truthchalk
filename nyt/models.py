from pymongo import MongoClient
client = MongoClient()
db = client.nyt
articles = db.articles