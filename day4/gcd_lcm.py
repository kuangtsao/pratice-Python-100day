x = int(input('x = '))
y = int(input('y = '))

for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公因數是%d' % (x, y, factor))
        print('%d和%d的最小公倍數是%d' % (x, y, x * y // factor))
        break

