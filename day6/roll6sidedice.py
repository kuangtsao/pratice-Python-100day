from random import randint

def roll_6_side_dice(n=2):
    """
    擲骰子

    :param n: 骰子個數
    ;return: n顆骰子和
    """
    sum = 0
    for _ in range(n):
        sum += randint(1, 6)
    return sum

def add (a=0, b=0, c=0):
    return a + b + c

print(roll_6_side_dice())
print(roll_6_side_dice(3))

print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(c=50, a=100, b=200))


