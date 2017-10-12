from pandas import Series, DataFrame

row_list = []
dict1 = {'Key': "Net Income", '2015': 100, '2016': 100, 'Comparision': 0}
row_list.append(dict1)
dict1 = {'Key': "Total Cash Flow", '2015': 100, '2016': 100, 'Comparision': 0}
row_list.append(dict1)

df = DataFrame(row_list, columns=['Key', '2015', '2016', 'Comparision'])
print(df)
