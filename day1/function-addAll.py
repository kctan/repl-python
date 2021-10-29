
def addAll(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(addAll(1, 2))

print(addAll(1, 2, 3, 4, 5, 6, 7, 8, 9))