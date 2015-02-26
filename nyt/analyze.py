from models import articles

# for x in articles.find({"byline": {"$not": {"$size": 0}}}):
# 	print x['byline']

# for x in articles.find({"byline.person": {"$not": {"$size": 0}}}):
# 	print x['byline']

# no size 2
# for x in articles.find({"byline.person": {"$size": 1}}):
# 	print x['byline']

# for name in articles.distinct('byline.original'):
# 	print name, articles.find({"byline.original": name}).count()

for x in articles.aggregate([{"$group": {
	"_id": {"original": "$byline.original"},
	"numArticles": { "$sum": 1},
	"numSentences": { "$sum": {"$size": "$sentences"} }
}}])['result']:
	print x

# res = articles.aggregate([{"$group": { "_id": { "firstname": "$byline.person.firstname", "lastname": "$byline.person.lastname", "original": "$byline.original"}}}])
# if res['ok'] == 1.0:
# 	for x in res['result']:
# 		person = x['_id']
# 		print person['original'], articles.find({"byline.original": person['original']}).count()