from unittest import TestCase
from string_parser import StringParser
from nodes import *

class TestStringParser(TestCase):
	def test_parse_literal_string(self):
		def hello(): pass
		parser = StringParser()
		parser.register(Sequence([LiteralString("Hello")],hello))
		function, arguments = parser.parse("Hello")
		self.assertEqual(function, hello)
		self.assertEqual(arguments, [])
		
	def test_parse_multiple_literal_string(self):
		def hello_world(): pass
		parser = StringParser()
		parser.register(Sequence([LiteralString("Hello"),LiteralString("World")],hello_world))
		function, arguments = parser.parse("Hello World")
		self.assertEqual(function, hello_world)
		self.assertEqual(arguments, [])
