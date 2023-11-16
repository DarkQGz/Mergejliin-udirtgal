for num in range(2, 10001):
    a = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            a = False
            break
    if a:
        print(num)
