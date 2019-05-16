def add(*args):
    sum = 0
    for val in args:
        sum += val
    return sum

print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
