#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse

import xml.sax

import xml.dom.minidom
from xml.dom.minidom import parse

class BookHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.current = ""
		self.author = ""
		self.title = ""
		self.genre = ""
		self.price = ""
		self.publish_date = ""
		self.description = ""
#  Start element
	def startElement(self, tag, attrs):
		self.current = tag
		if tag == "book":
			print(f"-- Book {attrs['id']} --")
# Printing if the text is correct
	def endElement(self, tag):
		if self.current == "author":
			print(f"author: {self.author}")

		elif self.current == "title":
			print(f"title: {self.title}")

		elif self.current == "genre":
			print(f"genre: {self.genre}")

		elif self.current == "price":
			print(f"price: {self.price}")

		elif self.current == "publish_date":
			print(f"publish_date: {self.publish_date}")

		elif self.current == "description":
			print(f"description: {self.description}")

		self.current = ""
# Inside elements save
	def characters(self, content):
		if self.current == "author":
			self.author = content

		elif self.current == "title":
			self.title = content

		elif self.current == "genre":
			self.genre = content

		elif self.current == "price":
			self.price = content

		elif self.current == "publish_date":
			self.publish_date = content

		elif self.current == "description":
			self.description = content



if (__name__ == "__main__"):
	print("\n\n\nsax\n\n")
	# XMLReader
	parser = xml.sax.make_parser()
	# turn off namepsaces
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)

	#ContextHandler
	Handler = BookHandler()
	parser.setContentHandler(Handler)

	parser.parse("file:///home/user/Documents/studia/Rok4/s7/pyton/lab/cw6/books.xml")


	print("\n\n\ndom\n\n\n")
	DOMTree = xml.dom.minidom.parse("/home/user/Documents/studia/Rok4/s7/pyton/lab/cw6/books.xml")
	group = DOMTree.documentElement
	books = group.getElementsByTagName("book")
	for book in books:
		print(f"-- Book {book.getAttribute('id')} --")
		author = book.getElementsByTagName('author')[0].childNodes[0].nodeValue #Get get the first one found, and the the value(by child node)
		title = book.getElementsByTagName('title')[0].childNodes[0].nodeValue
		genre = book.getElementsByTagName('genre')[0].childNodes[0].nodeValue
		price = book.getElementsByTagName('price')[0].childNodes[0].nodeValue
		publish_date = book.getElementsByTagName('publish_date')[0].childNodes[0].nodeValue
		description = book.getElementsByTagName('description')[0].childNodes[0].nodeValue

		#Printing
		print(f"author: {author}")
		print(f"title: {title}")
		print(f"genre: {genre}")
		print(f"price: {price}")
		print(f"publish_date: {publish_date}")
		print(f"description: {description}")

	#Changing one tag
	books[0].getElementsByTagName('author')[0].childNodes[0].nodeValue = "New Autor"
	books[0].setAttribute("id", "200")
	