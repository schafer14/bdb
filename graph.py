# Graph inherits from builtin type dinc -> for dictionary
class Graph(dict):
	def __init__(self, nodes=[], edges=[]):
		# create a new graph
		for node in nodes:
			self.add_node(node)

		for edge in edges:
			self.add_edge(edge)

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
		return this.keys()

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
				return nodes

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
    v = Node({'Name':'Banner'})
    w = Node({'Name':'Casey'})
    x = Node({'Name':'Joey'})
    z = Node({'Name': 'Lenny'})
    a = Node({'Name': 'Sean'})
    b = Node({'Name': 'Colin'})
    c = Node({'Name': 'Reed'})
    d = Node({'Name': 'Kim'})

    e = Edge('Friend', v, x)
    e1 = Edge('Friend', x, v)
    e2 = Edge('Brother', v, w)
    e3 = Edge('Brother', w, v)
    e4 = Edge('Brother', x, z)
    e5 = Edge('Brother', z, x)
    e6 = Edge('Brother', a, b)
    e7 = Edge('Brother', b, a)
    e8 = Edge('Friend', v, a)
    e9 = Edge('Mother', c, d)
    e10 = Edge('Friend', v, c)

    

    g = Graph([v,w,x,z,a,b,c,d], [e, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10])

    print g.link(w, 'Brother->Friend->Mother')

if __name__ == '__main__':
    import sys
    main(*sys.argv)