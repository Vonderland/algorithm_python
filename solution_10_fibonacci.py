# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n < 0:
            return -1
        else:
            fibonacci = [0, 1]
            while len(fibonacci) <= n:
                fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci[n]