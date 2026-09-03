""" 本次改进主要是改进了条件判断的语句，
使代码更加的简洁
"""

class Solution(object):
    def lengthOfLastWord(self,s):
        total_length = len(s) # 记录整个字符串的长度
        left = 0 # left用于记录同一个单词最开头那个字母的索引下标
        right = 0 # right用于记录同一个单词最后那个字母的索引下标
        for i in range(total_length): # 由于单词会相互覆盖，因此得到的就是最后一个单词的开头和结尾字母的索引下标
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '): # 单词开头字母要满足自身不为空格，且前一个字符（若存在）要为空格
                left = i
            if s[i] != ' ' and (i == len(s)-1 or s[i+1] == ' '): # 单词末尾字母要满足自身不为空格，且后一个字符（若存在）要为空格
                right = i
        return right - left + 1 # 注意要加1的操作