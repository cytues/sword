# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # 直接使用python特性，将空格替换成想要的字符串
        return s.replace(' ', '%20')
