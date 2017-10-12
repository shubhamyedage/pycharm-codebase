import numpy as np
import matplotlib.pyplot as plt
from os.path import expanduser, join


width = 0.1       # the width of the bars

l1 = [2665,	3599,	4607,	5259,	5886, 2665,	3599,	4607,	5259,	5886, 6666]

l2 = [8719,	7509,	9072,	9659,	10825, 8719,	7509,	9072,	9659,	10825, 11111]
x_data = np.arange(1, len(l1)+1)
print(len(x_data))
print(x_data)

x_ticks = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x_data, l1, width, color='g', fill=False, edgecolor='g')

rects2 = ax.bar(x_data + width, l2, width, color='r')

# add some text for labels, title and axes ticks
ax.set_ylabel("Index", fontsize=12)
ax.set_title("C1 vs C2", fontsize=12)
# ax.set_xticklabels(x_ticks)
# print(plt.xlim())
# plt.xlim(xmin=0.22)
# print(plt.xlim())
plt.xticks(x_data, x_ticks)
ax.legend((rects1[0], rects2[0]), ('C1', 'C2',), loc='upper right')
plt.savefig(join(expanduser('~'), 'PycharmProjects', 'Test', 'docs', 'test2.png'))
plt.show()
