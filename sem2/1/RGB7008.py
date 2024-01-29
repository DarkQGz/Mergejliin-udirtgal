x = int(input())
def func(c):
    y= (x % 100)
    z = x % 10
    b = (y-z) / 10
    return b
b = func(x)
print (int(b))
