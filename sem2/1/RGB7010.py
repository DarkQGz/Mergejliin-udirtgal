x = int(input())
def func(c):
    y=  x % 100
    z = x % 10
    b = (y-z) / 10

    c = (x-y) / 100

    p = b+c+z
    return p
p = func(x)
print (int(p))
