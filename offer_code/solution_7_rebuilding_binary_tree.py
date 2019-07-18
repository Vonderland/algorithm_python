# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root_val = pre[0]
        root = TreeNode(root_val)
        if len(pre) == 1:
            return root
        root_index = tin.index(root_val)
        if root_index > 0:
            root.left = self.reConstructBinaryTree(pre[1:1 + root_index], tin[:root_index])
        right_length = len(tin) - root_index - 1
        if right_length > 0:
            root.right = self.reConstructBinaryTree(pre[1 + root_index:], tin[root_index + 1:])
        return root