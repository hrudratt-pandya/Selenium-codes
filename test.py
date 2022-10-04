import datetime

dt = datetime.datetime.now()

print(dt)
# 1970-01-01 09:00:00

# print(type(dt))
# <class 'datetime.datetime'>

print(dt.strftime('%s'))