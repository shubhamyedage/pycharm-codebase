import calendar
from datetime import date, datetime

print(datetime.now().date())
dat = datetime.now().date().strftime("%Y-%m")
print(dat)
print(type(dat))

dt = datetime.strptime(dat, "%Y-%m")
print(dt)

# yr = dt.year
# mon = dt.month
# md = calendar.monthrange(yr, mon)
# print("################")
# print(type(md))
# print(md)
#
# dat_1 = date(yr, md[0], md[1])#.strftime("%d-%m-%Y")
# print(dat_1)
