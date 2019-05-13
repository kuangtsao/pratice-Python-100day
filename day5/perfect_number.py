"""
找出1~9999的所有完美數
完美數是除了自身以外所有因數和為自身的數

解法：實實在在的找因數(divisor)，然後相加作判斷

1.找因數，並排除本身
2.相加得解，判斷是否為自身

"""

for perfect in range(1,10000):
    sum = 0
    for divisor in range(1, perfect):
        if perfect % divisor == 0:
            sum += divisor
            if sum == perfect + 1:
                print(sum)
        




