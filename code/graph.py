import random
import math


# Graph inherits from builtin type dinc -> for dictionary
class Graph(dict):
	def __init__(self, nodes=[], edges=[], bi_edge=[]):
		# create a new graph
		for node in nodes:
			self.add_node(node)

		for edge in edges:
			self.add_edge(edge)

		for edge in bi_edge:
			self.add_bi_edge(edge)

	def add_node(self, node):
		# add node to the graph
		self[node] = {}

	def add_edge(self, edge):
		# add edge to the graph
		s, v, w = edge
		self[v][w] = edge

	def add_bi_edge(self, edge):
		# add edge to the graph
		s, v, w = edge
		self[v][w] = edge
		self[w][v] = edge

	def nodes(self):
		return self.keys()

	def edges(self):
		return [self[n1][n2] for n1 in self for n2 in self[n1] if n2 in self[n1]]

	def add_random_edges(self, p):
		total = len(self)
		edges = total * (total-1) / 2 * p
		edge = 0
		nodes = self.nodes()
		while (edge < edges):
			r1 = nodes[int(math.floor(random.random() * total))]
			r2 = nodes[int(math.floor(random.random() * total))]
			if (r1 != r2):
				try:
					self[r1][r2]
				except:
					self.add_edge(Edge('', r1, r2))
					edge = edge + 1
		return None

	def dunbar_random_edges(self):
		total = len(self)
		edges = total * 150
		edge = 0
		nodes = self.nodes()
		while (edge < edges):
			r1 = nodes[int(math.floor(random.random() * total))]
			r2 = nodes[int(math.floor(random.random() * total))]
			if (r1 != r2):
				try:
					self[r1][r2]
				except:
					self.add_edge(Edge('', r1, r2))
					edge = edge + 1
		return None

	def link(self, node, param=None):
		if param == None:
			return [n1 for n1 in self if self[node].__contains__(n1)]
		if type(param) == str:
			param = param.split('->')
			if len(param) == 1:
				return [n1 for n1 in self if self[node].__contains__(n1) and self[node][n1][0] == param[0]]
			else:
				nodes = []
				p = param.pop(0)
				for n1 in self[node].keys():
					if self[node].__contains__(n1) and self[node][n1][0] == p:
						nodes.extend(self.link(n1, '->'.join(param)))
				return unique(nodes)
		if type(param) == int:
			if param == 1:
				return [n1 for n1 in self if self[node].__contains__(n1)]
			else:
				nodes = []
				for n1 in self[node].keys():
					nodes.extend(self.link(n1, param - 1))
				return unique(nodes)

	def add_all_edges(self):
		for n1 in self:
			for n2 in self:
				if (n1 != n2):
					e = Edge('', n1, n2)
					self.add_edge(e)


def unique(seq):
	set = {}
	map(set.__setitem__, seq, [])
	return set.keys()

# Inherits from object class
class Node(object):
	def __init__(self, label=''):
		self.label = label

	# repr retruns a string repersentation of the node object
	def __repr__(self):
		try:
			return 'Node: %s' % self.label['Name']
		except:
			return 'Node: %s' % self.label
		

	__str__ = __repr__


# Inherits from tuple class
# Immutable class
class Edge(tuple):
	# override on builtin new for tuple class
	def __new__(cls, str, e1, e2):
		return tuple.__new__(cls, (str, e1, e2))

	def __repr__(self):
		# print the repersentation of each node
		return '%s: (%s, %s)' % (self[0], repr(self[1]), repr(self[2]))

	__str__ = __repr__

def main(script, *args):
	print 'main'

if __name__ == '__main__':
    import sys
    main(*sys.argv)