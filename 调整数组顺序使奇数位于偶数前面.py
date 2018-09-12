# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        # 创建两个列表，分别存储奇数和偶数
        lst1 = []
        lst2 = []
        for i in array:
            # 奇数添加进lst1，偶数添加进lst2
            if i % 2 == 1:
                lst1.append(i)
            else:
                lst2.append(i)
        # lst1在前，即奇数在偶数前
        return lst1 + lst2