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

    def duplicate_not_change(self, numbers, duplication):
        start = 1
        end = len(numbers) -1
        while start <= end:
            middle = start + (end - start) // 2
            count = self.count_times(numbers, start, middle)
            if start == end:
                if count > 1:
                    duplication[0] = start
                    return True
                else:
                    break
            if count > middle - start + 1:
                end = middle
            else:
                start = middle + 1
        return False

    def count_times(self, numbers, start, end):
        if len(numbers) > 0:
            flag = [n >= start and n <= end for n in numbers]
            return sum(flag)
        else:
            return 0