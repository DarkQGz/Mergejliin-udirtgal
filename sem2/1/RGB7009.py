x = int(input())
def func(c):
    y= (x % 100)
    z = x % 10
    b = (y-z) / 10

    c = x % 10

    p = b*c
    return p
p = func(x)
print (int(p))
