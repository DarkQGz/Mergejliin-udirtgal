for i in range(1, 10001, 1):
    a = 0
    for n in range (1, j, 1):
        if (i%n==0):
            a+=n
    if(i==a):
        print(i)
