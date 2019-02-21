
from instaphyte import Instagram
import re

api = Instagram()

hashtag, n = input("Hashtag: "), int(input("Number of posts: "))

with open(hashtag + ".txt", 'w+') as f:
	for post in api.hashtag(hashtag, n):
		if len(post['node']['edge_media_to_caption']['edges']) < 1:
				continue
		contents = str(post['node']['edge_media_to_caption']['edges'][0]['node']['text'])

		cleaned_contents = re.sub(r"[^a-zA-Z0-9\såæøÅÆØ]"," ",contents) #only allow these characters

		f.write(cleaned_contents + "\n\n")
