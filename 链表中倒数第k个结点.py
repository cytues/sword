# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
思路：遍历整个链表，将链表的值添加进列表中，使用lst[-k]来逆序显示
'''
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        lst = []
        while head:
            lst.append(head)
            head = head.next
        if not head:
            return

        return lst[-k]