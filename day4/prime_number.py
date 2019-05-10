num = int(input('請輸入一個正整數：'))
is_prime = True

for x in range(2, num):
    if num % x == 0:
        is_prime = False
        print(is_prime)
        break
if is_prime and num != 1:
    print('%d是質數' % num)
else:
    print('%d不是質數' % num)

    

