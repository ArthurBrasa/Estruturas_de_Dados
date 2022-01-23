x1 = 5
x2 = '5.0'
x3 = float(x2)
x4 = int(x3)
x5 = x1 == x4
x1 = x5
x2 = x3
x3 = str(x5)
x4 = x2 / x2
x5 = -x5
print(type(x5))