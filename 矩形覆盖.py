# -*- coding:utf-8 -*-
'''
依旧是斐波那契数列
2*n的大矩形，和n个2*1的小矩形
其中 2*target 为大矩阵的大小
有以下几种情形：
1⃣️target <= 0 大矩形为<= 2*0,直接return 1；
2⃣️target = 1大矩形为2*1，只有一种摆放方法，return1；
3⃣️target = 2 大矩形为2*2，有两种摆放方法，return2；
4⃣️target = n 分为两步考虑：
# 竖着摆放
第一次摆放一块 2*1 的小矩阵，则摆放方法总共为f(target - 1)
√
√
# 横着摆放（有上下两种情况）
第一次摆放一块1*2的小矩阵，则摆放方法总共为f(target-2)
因为，摆放了一块1*2的小矩阵（用√√表示），对应下方的1*2（用××表示）摆放方法就确定了，所以为f(target-2)
√	√
×	×
target >= 3  f(n) = f(target - 1) + f(targte-2)
'''
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        else:
            res = [0, 1, 2]
            while len(res) < number:
                res.append(res[-1] + res[-2])

            return res[number]



