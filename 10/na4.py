n = int(input())
if n>1:
    s=True
    for i in range (2,int(n**0.5)+1):
        if n % i == 0:
            s=False
            break
    if s:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
