"""
找出1~9999的所有完美數
完美數是除了自身以外所有因數和為自身的數

解法：實實在在的找因數(divisor)，然後相加作判斷

1.找因數，並排除本身
2.相加得解，判斷是否為自身

"""

for number in range(1,10000):
    sum = 0
    for divisor in range(1, number):
    #range -> 1 <= divisor < number ，恰好可排除自身  
        if number % divisor == 0:
            sum += divisor            
    if sum == number:
        print(number)
    #為何要放在第一層？原因就是我們要找那個數字而非因數！    




