from nltk.tokenize import sent_tokenize
from models import articles

if __name__ == "__main__":

	for i, article in enumerate(articles.find({"sentences": {"$exists": False}})):
		print i, article['headline']['main'], article['_id']
		article['sentences'] = sent_tokenize(article['text'])
		articles.save(article)