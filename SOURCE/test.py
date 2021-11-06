from model import *

node = Node(5)
frontier = [(2,Node(3)), (1,Node(2)), (4,Node(5))]

print(node in frontier)