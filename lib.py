import os
import urllib2
import urllib
from parser import Parser
from selenium import webdriver
import re

# create a directory if it does not exist

def create_directory(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

# create a new file and write to it

def create_file(file_name):
	if not os.path.isfile(file_name):
		f = open(file_name, 'w')
		f.close()

# open a webpage url and return its result

def open_page(page_url):
	browser = webdriver.PhantomJS()
	browser.get(page_url)
	html = browser.page_source
	return html

# appending content to file

def append_file(file, content):
	with open(file, 'a') as file:
		file.write(content + '\n')

# set of images to file

def set_to_file(images, file):
	for image in sorted(images):
		append_file(file, image)

# start the program

def init(PROJECT_NAME, WEB_URL):
	FILENAME = PROJECT_NAME + '/images.txt'
	html = open_page(WEB_URL)
	create_directory(PROJECT_NAME)
	create_file(FILENAME)
	feeder = Parser(WEB_URL)
	feeder.feed(html)
	IMAGE_SET = feeder.image_links()
	set_to_file(IMAGE_SET, FILENAME)
	print('Done parsing check : ' + FILENAME)