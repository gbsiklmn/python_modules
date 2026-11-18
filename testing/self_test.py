import math
a, b, c = map(float, input().split())

length = round(math.sqrt (a ** 2 + b ** 2 + c**2), 2)
print(length)