import time
n = int(input())
s = time.time()
for num in range(2, n + 1):
    a = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            a = False
            break
    if a:
        print(num)
g = time.time()
e = g - s
print(f"{e:.2f}")
