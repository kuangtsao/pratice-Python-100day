import random

answer = random.randint(1, 100)
counter = 0

while True:
    counter += 1
    number = int(input('請輸入：'))
    if number < answer:
        print('數字比較大')
    elif number > answer:
        print('數字比較小')
    else:
        print('jackpot!')
        break
print('猜了%d次' % counter) 
if counter > 7:
    print('猜太多次，嫩！')
