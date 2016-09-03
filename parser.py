from HTMLParser import HTMLParser
from urlparse import urljoin

class Parser(HTMLParser):

	def __init__(self, base_url):
		HTMLParser.__init__(self)
		self.base_url = base_url
		self.images = set()

	def handle_starttag(self, tag, attrs):
		if tag == 'img':
			for (attribute, value) in attrs:
				if attribute == 'src':
					url = urljoin(self.base_url, value)
					self.images.add(url)

	def image_links(self):
		return self.images