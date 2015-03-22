import sys
import unicodecsv as csv
from models import articles

if __name__ == "__main__":

	fieldnames = ['_id', 'headline', 'index', 'sentence', 'word_count', 'web_url', 'keywords', 'pub_date', 'byline', 'will', "won't"]

	with open("articles.csv", "w") as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
		for article in articles.find():
			for i, sentence in enumerate(article['sentences']):
				d = {k:v for k,v in article.iteritems() if k in fieldnames if k in article}
				d['index'] = i
				d['sentence'] = sentence
				d['headline'] = d['headline']['main']
				d['byline'] = d['byline']['original'] if d['byline'] != [] else ""
				d["will"] = "will" in d['sentence']
				d["won't"] = "won't" in d['sentence']
				writer.writerow(d)