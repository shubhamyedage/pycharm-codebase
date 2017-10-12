from os.path import join, expanduser
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

l1 = [2665,	3599,	4607,	5259,	5886]

l2 = [8719,	7509,	9072,	9659,	10825]
x_data = np.arange(1, len(l1)+1)
# x_ticks = ['a', 'b', 'c', 'd', 'e']
# plt.title("AMAT vs LRCX")
# plt.xticks(x_data, x_ticks)
# plt.plot(x_data, l1, 'red', x_data, l2, 'blue')
# plt.ylabel("Revenue", fontsize=12)
# p1 = patches.Patch(color='red', label='AMAT')
# p2 = patches.Patch(color='blue', label='LRCX')
# plt.legend(handles=[p1, p2])
# plt.savefig(join(expanduser('~'), 'PycharmProjects', 'Test', 'docs', 'test.png'))
# plt.show()

z = np.polyfit(x_data, l1, 1)
print(z[0])
print(z[1])
# new_l1 = [z[0]*x+z[1] for x in x_data]
# plt.plot(x_data, l1, 'r--', x_data, new_l1)
# plt.title("Revenue")
# plt.show()

# z = np.polyfit(x_data, l2, 1)
# print(z[0])
# new_l2 = [z[0]*x+z[1] for x in x_data]
# plt.plot(x_data, l2, 'r--', x_data, new_l2)
# plt.title("Revenue")
# plt.show()