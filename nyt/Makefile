exportmongo:
	mongoexport --db nyt --collection articles --out mongodata.json --journal --jsonArray

exportes:
	elasticdump --input=http://localhost:9200/articles --output=esdata.json --type=data

importes:
	curl -XPOST localhost:9200/articles/article/_bulk --data-binary @articles.json

createes:
	curl -XPUT 'http://localhost:9200/articles/'

deletees:
	curl -XDELETE 'http://localhost:9200/articles/'

clean:
	rm *.pyc
