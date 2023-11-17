a = int(input())
b = list(map(int, input().split()))
c = b[0]
for i in range(0, a, 1):
    if b[i]>c:
        c=b[i]
print(c)
