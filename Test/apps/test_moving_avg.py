from os.path import join, expanduser
import numpy as np
from matplotlib import pyplot as plt

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def rotate(a, n=1):
    for i in range(len(a) - n):
        a = a[1:] + a[:1]
        print(a)
    return a
# l = [8719,7509,9072,9659,10825]
y1 = [12102,	12043,	13174,	15308,	14588]
y2 = moving_average(y1, n=2)
np.append(y2, y1[0])
y2 = rotate(y2, 1)
print(y2)
x = np.arange(1, len(y2)+1)
plt.plot(x, y2, 'green')
plt.savefig(join(expanduser('~'), 'PycharmProjects', 'Test', 'docs', 'test.png'))
# plt.show()