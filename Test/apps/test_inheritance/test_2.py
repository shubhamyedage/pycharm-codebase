class Parent():
    def __init__(self, nm=''):
        self.name = nm

    def get_surname(self):
        return "surname"

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)

    def my_surname(self):
        s = self.get_surname()
        print(s)


p = Parent('Parent')
child = Child()
print(child.name)
child.my_surname()
