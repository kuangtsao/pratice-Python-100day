"""
求費布納希數列的前20個數
"""

a = 0
b = 1

for _ in range(20):
    (a, b) = (b ,a+b)
    print(a, end=' ')
