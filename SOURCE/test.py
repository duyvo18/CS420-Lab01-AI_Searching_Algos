from model import *

test = "3 4 2 5"
a = []
for e in test.split(" "):
    a.append(int(e))
a.sort()
a.reverse()
print(a)