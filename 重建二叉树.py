# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    # 根据前序遍历和中序遍历重建二叉树
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        # 遇到树的问题优先考虑使用递归
        # pre为前序遍历，tin为中序遍历
        if not pre or not tin:
            return None
        # 前序遍历的第一个值为根节点
        root = TreeNode(pre[0])
        # 在中序遍历中找到根节点,也是中心位置
        val = tin.index(pre[0])
        # 递归调用函数，遍历两个序列
        # 原树的左子树：前序遍历（从根节点一直到中心点），中序遍历（从开头一直到中心位置）
        root.left = self.reConstructBinaryTree(pre[1:val + 1], tin[:val])
        # 原树的右子树：前序遍历（从中心点后一直到叶子节点），中序遍历（同前序）
        root.right = self.reConstructBinaryTree(pre[val + 1:], tin[val + 1:])

        return root