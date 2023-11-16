for a in range(2, 10001):
    d = 1 + sum(i + a // i for i in range(2, int(a**0.5) + 1) if a % i == 0 and i != a // i)
    if a == d: print(a)
