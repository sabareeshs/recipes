from html.parser import HTMLParser
import urllib.request, urllib.error, urllib.parse


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	def download(self, url):
		print ("Downloading", url)
		recipeId = url[url.find('recipes/') + 8: ]
		print ("RecipeId", recipeId)
		
		response = urllib.request.urlopen(url)
		webContent = response.read()
		f = open('recipes/' + recipeId, 'wb')
		f.write(webContent)
		f.close

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for attr, data in attrs:
				if attr == "href" and data.find('search') == -1 and data.find('recipes') != -1 and data.find('veggie') != -1:
					 self.download(data[:-9])
					 return

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
with open('recipes_hello_fresh_raw.htm', 'r') as file:
    data = file.read().replace('\n', '')
parser.feed(data)
