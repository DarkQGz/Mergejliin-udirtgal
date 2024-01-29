seconds = int(input())
def func(c):
    minutes = seconds // 60
    return minutes
def funcc(c):
    remaining_seconds = seconds % 60
    return remaining_seconds
minutes = func(seconds)
remaining_seconds = funcc(seconds)
print (minutes, remaining_seconds)
