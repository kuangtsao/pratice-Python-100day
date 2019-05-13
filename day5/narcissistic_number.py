"""
水仙花數

任一三位數等同於3位數各自的立方和

abc = a^3 + b^3 + c^3

100<= number <= 999

"""

for number in range(100,1000):

    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    units = (number // 1) % 10

    if number == hundreds ** 3 + tens ** 3 + units ** 3:
        print('%d= %d^3 + %d^3 + %d^3' % (number, hundreds, tens, units))


