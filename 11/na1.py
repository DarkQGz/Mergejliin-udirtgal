print(*[num for num in range(2, 10001) if all(num % i for i in range(2, int(num**0.5) + 1))], sep='\n')
