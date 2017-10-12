l1 = []
l2 = [1,2,3,4]
l3 = [1,2,3,4]
l4 = [0]

l1 = [(a+b+c) for a, b,c in zip(l2,l3,l4)]
# print(l1)

l4 = [0 for i in range(5)]
# print(l4)


########### Test for order ###########
l = []
l.append("s")
l.append("a")
l.append("v")

for s in l:
    print(s)