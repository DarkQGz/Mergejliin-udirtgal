import sys
sys.stdin = open("Suum.in", "r")
sys.stdout = open("Suum.out", "w")
n = int(input())
nlist= list(map(int, input().split()))
o = int(input())
olist= list(map(int, input().split()))
s = int(input())
slist= list(map(int, input().split()))
sums = 0
for i in range(0, n, 1):
    sums+=nlist[i]
urj = 1
for i in range(0, o, 1):
    urj*=olist[i]
max1 = max(slist)
print(sums)
print(urj)
print(max1)
