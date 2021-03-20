class Sequence:
	def __init__(self, nodes, function):
		self.nodes = nodes
		self.function = function
	
	def parse(self, string):
		arguments = []
		for node in self.nodes:
			argument, string = node.parse(string)
			if argument != None: arguments.append(argument)
		if string == "":
			return self.function, arguments
		raise SyntaxError()

class LiteralString:
	def __init__(self, string):
		self.string = string
	
	def parse(self, string):
		if string == self.string:
			return None, ""