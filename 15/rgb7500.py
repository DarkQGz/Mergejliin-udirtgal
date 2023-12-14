import sys
sys.stdin = open("7500.in", "r")
sys.stdout = open("7500.out", "w")
l = []
a = int(input())
c = 0
for i in range(0, a, 1):
    b = int(input())
    l.append(b)
for i in range(0, a, 1):
    c+=l[i]
print(c)
