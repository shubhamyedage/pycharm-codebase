from collections import OrderedDict

m = OrderedDict([
    ('d', 4),
    ('a', 5)
])


print(m.get('d'))
print("##############")
for k, v in m.items():
    print(k)
    print(v)