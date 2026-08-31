""" 相较于最初的版本，这次优化主要是为了简化代码，
更加体现字典（哈希表）在此类问题中的应用。
"""


# 题目要求 s.length >= 1
class Solution(object):
    def isValid(self, s):
        dic = {']': '[', '}': '{', ')': '('}  # 构建一部字典（哈希表），方便后续的匹配操作
        s1 = "{[("
        stack = []  # 构建一个列表（栈），利用遇到左括号入栈，遇到右括号出栈并进行匹配的思路解决这一问题
        for c in s:
            if c in s1:  # c 为左括号时
                stack.append(c)  # 入栈操作
            else:
                if not stack or dic[c] != stack.pop():  # 如果遇到右括号时栈为空(此时不能进行出栈操作)则括号不匹配
                    return False  # 或者遇到的右括号和最近的左括号不匹配则括号不匹配

        return stack == []  # 只有左括号残留则括号不匹配
