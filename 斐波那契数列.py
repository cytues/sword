# -*- coding:utf-8 -*-
'''
使用递归会超时
'''
class Solution:
    def Fibonacci(self, n):
        # write code here
        # fib数列小于3的值为0，1，1
        res = [0, 1]
        while len(res) <= n:
            res.append(res[-1] + res[-2])

        return res