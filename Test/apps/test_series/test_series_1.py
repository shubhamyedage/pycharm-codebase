import pandas as pd

d = [1,2,3,4]
i = ['a','b','c','d']

s = pd.Series(d, index=i)
print(s)
print(s.get('a'))
print(s.keys().tolist())
print(s.values)