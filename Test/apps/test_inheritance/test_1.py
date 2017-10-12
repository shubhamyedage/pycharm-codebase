class FemaleGrandParent:
    def __init__(self):
        self.grandma_name = "Grandma"

class MaleGrandParent:
    def __init__(self, grandpa):
        self.grandpa_name = grandpa

class Parent(MaleGrandParent, FemaleGrandParent):
    def __init__(self, grandpa):
        MaleGrandParent.__init__(self, grandpa)
        FemaleGrandParent.__init__(self)
        self.parent = "Parent"

class Child(Parent):
    def __init__(self, grandpa):
        Parent.__init__(self, grandpa)
        self.child = "Child"

child = Child("Grandpa")
print(child.grandpa_name)