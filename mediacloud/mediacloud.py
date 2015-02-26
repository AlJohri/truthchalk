from __future__ import unicode_literals, print_function, division
import os, json, requests

BASE_URL = "https://api.mediacloud.org/api/v2/"

if __name__ == "__main__":

	# media.json -> https://api.mediacloud.org/api/v2/media/list/
	media_ids = {x['name'] : x['media_id'] for x in json.load(open("media.json"))}

	s = requests.Session()
	s.params.update({"key": os.getenv('MEDIACLOUD_API_KEY')})

	story_list_params = {"q": "media_id:%s" % media_ids['New York Times']}
	story_list = s.get(BASE_URL + "stories/list/", params=story_list_params).json()
	print(json.dumps(story_list, sort_keys=True, indent=4))