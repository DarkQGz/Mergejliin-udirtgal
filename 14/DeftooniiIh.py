def tooniiIh(a,b):
  if a <= b:
    c = b
  else:
    c = a
  return c
x,y=map(int , input().split())
k = tooniiIh(x,y)
print(k)
