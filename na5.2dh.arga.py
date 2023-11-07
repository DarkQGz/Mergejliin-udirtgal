num = int(input())
a = sum([i for i in range(1, num) if num % i == 0])
if a == num:
    print("Yes")
else:
    print("No")
