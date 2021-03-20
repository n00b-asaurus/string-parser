class StringParser:
	def __init__(self):
		self.parse_trees = []
		
	def register(self,tree):
		self.parse_trees.append(tree)
		
	def parse(self, string):
		for tree in self.parse_trees:
			return tree.parse(string)