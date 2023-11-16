import time
n, s = int(input()), time.time()
for a in range(2, n + 1):
    d = sum(i + a // i for i in range(2, int(a**0.5) + 1) if a % i == 0) + 1
    if a == d: print(a)
print(f"{time.time() - s:.2f}")
