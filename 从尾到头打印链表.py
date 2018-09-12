# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    # 该题思路：创建一个空列表，用来存储链表中的值，最后将列表逆序输出
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []

        result = []
        while listNode.next is not None:
            # extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
            result.extend([listNode.val])
            listNode = listNode.next
        result.extend([listNode.val])

        return result[::-1]