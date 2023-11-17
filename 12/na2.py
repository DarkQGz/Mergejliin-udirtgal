n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
su = 0
for num in numbers:
    if num > 0:
        su += num
print(su)
