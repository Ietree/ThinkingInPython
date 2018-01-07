# -*- coding: utf-8 -*-

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

max = input('please input the max value:')
print(fib(max))
