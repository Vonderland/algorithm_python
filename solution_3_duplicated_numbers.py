# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        i = 0
        while i < len(numbers):
            num = numbers[i]
            if num != i:
                if numbers[num] == num:
                    duplication[0] = num
                    return True
                else:
                    numbers[i], numbers[num] = numbers[num], num
            else:
                i += 1
        return False