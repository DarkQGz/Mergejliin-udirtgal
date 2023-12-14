n = int (input())

nlist = list (map (int, input().split()))

K = int(input())

klist = list (map(int, input().split()))

S = int (input())

Slist = list(map (int, input().split()))

sums=0

for i in range(0, n, 1): 
    sums = sums+nlist[i]
urj=1
for i in range (0,K, 1): 
    urj=urj * klist[i]
    
print(sums)
print(urj)
