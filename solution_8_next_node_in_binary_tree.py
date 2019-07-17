# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        # 有右子树，找右子树的最左子节点
        if pNode.right:
            pNext = pNode.right
            while pNext.left:
                pNext = pNext.left
            return pNext
        # 没有右子树
        # 且该节点为其父节点的左节点，下一个节点则是父节点
        pParent = pNode.next
        if pParent and pNode == pParent.left:
            pNext = pParent
            return pNext
        # 且该节点为其父节点的右节点，则沿着父节点向上找，找到是它父节点的左子节点的节点,
        # 这样的节点的父节点就是所求节点
        elif pParent and pNode == pParent.right:
            while pNode.next and pNode != pNode.next.left:
                pNode = pNode.next
        return pNode.next
