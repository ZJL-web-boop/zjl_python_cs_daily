"""本次改进不同于以往两个版本，前两个版本是从前往后遍历字符串，
但这道题要的是最后一个单词的长度，所以从后往前遍历可能会更好
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s)-1 # 从后面开始遍历
        while i >= 0 and s[i] == ' ': # 自动跳过空格
            i -= 1
        length = 0 # 记录最后一个单词的长度
        while i >= 0 and s[i] != ' ': #数到下一个空格或开头为止
            length += 1
            i -= 1
        return length
