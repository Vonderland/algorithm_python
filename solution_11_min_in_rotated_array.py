# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray or len(rotateArray) == 0:
            return 0
        index = 1
        while index < len(rotateArray):
            if rotateArray[index] < rotateArray[index - 1]:
                return rotateArray[index]
            index += 1
        return rotateArray[0]   

