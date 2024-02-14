from calendar import *
year, month = map(int, input().split())
d = monthrange(year, month)[1]
print(d)