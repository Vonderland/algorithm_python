# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # 总行列数
        if not array or not isinstance(array, list):
            return False
        rows = len(array)
        cols = len(array[0])
        # 从右上角开始搜索
        row, col = 0, cols - 1
        while row < rows and col >= 0:
            if target == array[row][col]:
                return True
            elif target < array[row][col]:
                col -= 1
            else:
                row += 1
        return False