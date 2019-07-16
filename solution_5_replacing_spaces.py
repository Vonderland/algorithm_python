# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        words = s.split(" ")
        s = ""
        for c in words:
            s += c + "%20"
        s = s[:-3]
        return s

    def lazyReplaceSpace(self, s):
        return s.replace(" ", "%20")