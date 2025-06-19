'''
fibonacci_recursif
'''


__author__ = "djelas_d"


def fibonacci(n: int):
    '''
    fibonacci_recursif
    '''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))  # 8
