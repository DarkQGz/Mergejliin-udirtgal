import time
n = int(input())
s = time.time()
for a in range(2, n + 1):
    d = 1  
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            d += i
            if i != a // i:  
                d += a // i
    if a == d:
        print(a)
e = time.time()
t = e - s
print(f"{t:.2f}")
