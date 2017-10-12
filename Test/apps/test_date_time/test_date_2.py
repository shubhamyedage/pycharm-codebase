"""
This module converts string to given date format.
Date-Time Formats
http://strftime.org/
"""
from datetime import datetime, date

s1 = "2008-08"
s2 = "2017-08"

v1 = datetime.strptime(s1, "%Y-%m")
# print(v1)
# print(v1.year)
v1_date = str(v1.date())
# print(datetime.strptime(v1_date, "%Y-%m-%d").date())


v2 = datetime.strptime(s2, "%Y-%m").date().strftime("%Y-%m")
print(v2)

v3 = datetime.now()
print(v3)


def get_year(d):
    return d.year


# y1 = get_year(v2)
y2 = get_year(v3)
# print(y1 == y2)

s = "feb-15"

v3 = datetime.strptime(s, "%b-%y")
# print("v3 : {v3}".format(v3=v3))
# print(v3.month)