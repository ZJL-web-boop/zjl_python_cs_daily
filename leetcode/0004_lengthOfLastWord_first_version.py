class Solution(object):
    def lengthOfLastWord(self,s):
        total_length = len(s) # 记录整个字符串的长度
        left = 0 # left用于记录同一个单词最开头那个字母的索引下标
        right = 0 # right用于记录同一个单词最后那个字母的索引下标
        for i in range(total_length): # 由于单词会相互覆盖，因此得到的就是最后一个单词的开头和结尾字母的索引下标
            if i == 0 and s[i] != ' ': # 字符串开头就是一个单词的情况（前面没有空格）
                left = i
            elif i+1 < total_length and s[i] == ' ' and s[i+1] != ' ': # 其它单词开头要满足的条件
                left = i+1
            if i+1 == total_length and s[i] != ' ': # 字符串结尾就是一个单词的情况（后面没有空格）
                right = i
            elif i+1 < total_length and s[i+1] == ' ' and s[i] != ' ': #其他单词结尾要满足的条件
                right = i
        return right - left + 1 # 注意要加1的操作