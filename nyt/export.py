import sys, json
from models import articles

if __name__ == "__main__":

	with open("articles.json", "w") as f:
		for article in articles.find():

			article = dict(article)
			command = {"index": {"_id": article['_id']}}
			del article["_id"]

			f.write(json.dumps(command) + "\n")
			f.write(json.dumps(article) + "\n")