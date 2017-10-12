
def f1():
    print("Hello")

def f2():
    print("Bye")

d = {'f1': f1,
 'f2': f2
 }

def do_action(choice):
    print("In do_action...")
    d.get(choice)()

do_action("f1")