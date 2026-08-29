class Solution:
    def longestCommonPrefix(self, strs):
        min_length = 200 # 题目要求：0 <= strs[i].length <= 200
        target = -1 # 以长度最短的字符串为目标进行寻找最长公共前缀的操作
        for i in range(len(strs)):
            if len(strs[i]) < min_length:
                min_length = len(strs[i])
                target = i
        end = min_length-1
        for i in range(len(strs)):
            for j in range(min_length):
                if strs[i][j] != strs[target][j]:
                    if j-1 < end:
                        end = j-1
        return strs[target][0:end+1]