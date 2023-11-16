for a in range(2, 10001):
    d = 1  
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            d += i
            if i != a // i:  
                d += a // i
    if a == d:
        print(a)
