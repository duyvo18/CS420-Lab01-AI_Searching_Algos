from model import *

a = (2, 'a')
print(type(a))

a: PQNode = (2, Node(3))
print(type(a))

b: FrontierPQ = [a, (1, 3), (5, 3), (2,4), (5, 1)]
print(b)
b.sort()
print(b)