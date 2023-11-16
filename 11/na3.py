import time
n, s = int(input()), time.time()
print(*[num for num in range(2, n + 1) if all(num % i for i in range(2, int(num**0.5) + 1))], sep='\n')
print(f"{time.time() - s:.2f}")
