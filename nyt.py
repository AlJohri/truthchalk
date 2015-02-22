import os, requests, lxml.html

BASE_URL = "http://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=%s" % os.getenv('NYT_API_KEY')

EDITORIAL_URL = BASE_URL + "&fq=news_desk:(%22Editorial%22)"

response = requests.get(EDITORIAL_URL)
hits = response.json()['response']['meta']['hits']

print "hits: ", hits

for page in xrange(hits / 10):
	url = EDITORIAL_URL + "&page=%d" % page
	articles = requests.get(url).json()['response']['docs']

	for article in articles:

		print article['headline']['main']

		response = requests.get(article['web_url'])
		doc = lxml.html.fromstring(response.content)
		text = "\n".join([x.text_content() for x in doc.cssselect("p.story-content")]).encode('latin-1')
		print text

		import pdb; pdb.set_trace()