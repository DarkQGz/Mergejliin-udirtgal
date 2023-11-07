num = int(input())
a = 0
for i in range(1, num):
    if num % i == 0:
        a += i
if a == num:
    print("Yes")
else:
    print("No")
