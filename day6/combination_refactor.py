def factorial(num):
    """
    求階乘
    :param num: 非負整數
    :return: num的階乘
    """
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result
m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m-n))
