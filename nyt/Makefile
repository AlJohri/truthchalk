exportmongodata:
	mongoexport --db nyt --collection articles --out mongodata.json --journal --jsonArray

exportesmapping:
	elasticdump --input=http://localhost:9200/articles --output=esmapping.json --type=mapping

exportesdata:
	elasticdump --input=http://localhost:9200/articles --output=esdata.json --type=data

importesdata:
	curl -XPOST localhost:9200/articles/article/_bulk --data-binary @articles.json

importesmapping:
	curl -XPUT 'http://localhost:9200/articles/_mapping/article' -d '
	{
	    "article" : {
	        "properties" : {
	            "_id" : {"type": "string"},
	            "type_of_material" : {"type": "string"},
	            "snippet" : {"type": "string"},
	            "news_desk" : {"type": "string"},
	            "lead_paragraph" : {"type": "string"},
	            "text" : {"type": "string"},
	            "abstract" : {"type": "string"},
	            "print_page" : {"type": "string"},
	            "pub_date" : {"type": "date"},
	            "word_count" : {"type": "integer"},
	            "blog" : {"type": "string"},
	            "source" : {"type": "string"},
	            "document_type" : {"type": "string"},
	            "web_url" : {"type": "string"},
	            "subsection_name" : {"type": "string"},
	            "section_name" : {"type": "string"},
				"headline.main" : {"type": "string"},
				"headline.kicker" : {"type": "string"},
				"headline.print_headline" : {"type": "string"},
				"headline.content_kicker" : {"type": "string"},
				"byline.contributor" : {"type": "string"},
				"byline.person" : {"type": "string"},
				"byline.original" : {"type": "string"}
	        }
	    }
	}
	'
deletees:
	curl -XDELETE 'http://localhost:9200/articles/'

