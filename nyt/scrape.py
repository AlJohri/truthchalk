import os, json, requests, lxml.html
from HTMLParser import HTMLParser
unescape = HTMLParser().unescape

from models import articles

BASE_URL = "http://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=%s" % os.getenv('NYT_API_KEY')
EDITORIAL_URL = BASE_URL + "&fq=news_desk:(%22Editorial%22)"
num_per_page = 10

if __name__ == "__main__":

	response = requests.get(EDITORIAL_URL)
	hits = response.json()['response']['meta']['hits']

	print "hits: ", hits

	for page in xrange(hits / 10):
		url = EDITORIAL_URL + "&page=%d" % page
		docs = requests.get(url).json()['response']['docs']

		for i, article in enumerate(docs):
			print page*num_per_page+i, unescape(article['headline']['main']), article['_id']
			response = requests.get(article['web_url'])
			doc = lxml.html.fromstring(response.content)
			text = "\n".join([x.text_content() for x in doc.cssselect("p.story-content")]).encode('latin-1')
			article['text'] = text
			article_id = articles.save(article)
			# print json.dumps(article, sort_keys=True, indent=4)