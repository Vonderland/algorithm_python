# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
    def push(self, node):
        self.stackA.append(node)
    def pop(self):
        if len(self.stackB):
            return self.stackB.pop()
        elif len(self.stackA):
            while len(self.stackA):
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()
        else:
            return None