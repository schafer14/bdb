from graph import Graph
from graph import Node
from graph import Edge

import random
import time

def small_db():
	v = Node({'Name':'Banner'})
	w = Node({'Name':'Casey'})
	x = Node({'Name':'Joey'})
	z = Node({'Name': 'Lenny'})
	a = Node({'Name': 'Sean'})
	b = Node({'Name': 'Colin'})
	c = Node({'Name': 'Reed'})
	d = Node({'Name': 'Kim'})
	
	c1 = Node({'Name': 'Amherst'})
	c2 = Node({'Name': 'Corvallis'})

	e = Edge('Friend', v, x)
	e1 = Edge('Brother', w, v)
	e2 = Edge('Brother', z, x)
	e3 = Edge('Brother', b, a)
	e4 = Edge('Friend', v, a)
	e5 = Edge('Friend', v, c)

	ce1 = Edge('Lives', b, c1)
	ce2 = Edge('Lives', z, c2)
	de = Edge('Mother', c, d)

	g = Graph([v,w,x,z,a,b,c,d,c1,c2], [de, ce1, ce2],[e, e1, e2, e3, e4, e5])

	print g.link(v, 'Friend->Brother->Lives')


def gen(inte=1000000):
	g = Graph()

	print 'Building graph.'
	for i in range(inte):
		g.add_node(Node(i))

	print 'Adding edges.'
	g.dunbar_random_edges()

	return g

def test(g, max_depth=5):
	num_nodes = len(g.nodes())
	node = g.nodes()[random.randrange(0, num_nodes - 1)]
	
	print 'Starting testing.'
	for depth in range(1, max_depth):
		start = time.clock()
		g.link(node, depth)
		print 'Depth ' + `depth` + ': ' + `(time.clock() - start)`
	
	return 

def main(script, *args):
	small_db()

	
if __name__ == '__main__':
	import sys
	main(*sys.argv)