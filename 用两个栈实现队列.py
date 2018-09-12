# -*- coding:utf-8 -*-
'''
A是入栈的，B是出栈的，入栈时，直接进入A即可，出栈时，先判断是否有元素，
如果B没有元素，pop肯定报错，应该先将A中所有的元素压倒B里面，再pop最上面一个元素，如果B中有就直接pop出，就可以，
这是最优的思路，两个栈实现了先进后出，在一起又实现了队列的先进先出。
'''
class Solution:
    # 初始化两个栈
    def __init__(self):
        self.stackA = []
        self.stackB = []
    # 这里只要求实现队列的push和pop操作，分别使用两个栈表示弹出和压入
    def push(self, node):
    # write code here
        self.stackA.append(node)
    # 弹出需要有一个先验条件：若队列为空，则返回None
    def pop(self):
        # 若压入的栈中有元素则直接弹出
        if self.stackB:
            self.stackB.pop()
        # 若A中没有元素则返回None
        elif not self.stackA:
            return None
        # 若A中有元素，则统一压入B中进行弹出
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()