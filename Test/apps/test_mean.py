import numpy as np
from matplotlib import pyplot as plt
from os.path import join, expanduser

# l = [12102,	12043,	13174,	15308,	14588]
# l = [1689,	426,	1559,	948,	2213]
l = [4867,4955,5306,7695,7371]
l = [(a-b)*100/b for a,b in zip(l[1:], l[:-1])]
print(l)

x = np.arange(1, len(l)+1)


z = np.polyfit(x, l, 1)
print(z[0])
print(z[1])

# l2 = [(z[0]*i+z[1]) for i in range(len(l))]
#
#
# plt.plot(x, l,'red',x,l2)
# plt.savefig(join(expanduser('~'), 'PycharmProjects', 'Test', 'docs', 'test.png'))
# plt.show()