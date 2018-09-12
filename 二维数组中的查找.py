# -*- coding:utf-8 -*-
# 时间复杂度为n^2
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # 不存在数组则直接返回
        if not array:
            return
        # 二维数组的行
        raw = len(array)
        # 二维数组的列
        col = len(array[0])
        # 二层循环遍历二维数组
        for i in range(raw):
            for j in range(col):
                # 如果目标值等于数组中的值，则找到
                if target == array[i][j]:
                    return True
        # 数组遍历结束后仍未找到
        return False