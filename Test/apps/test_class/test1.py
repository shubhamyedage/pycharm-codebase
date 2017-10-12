from operator import attrgetter

class Person(object):
    def __init__(self, name, val):
        self.val = val
        self.name = name



p = [Person('A', 1), Person('B', 2), Person('C', 3), Person('D', 3)]

an = max(p, key=attrgetter('val'))
print(an.val)

# p = [1,2,2,2,4,5,5]
# print(max(p))