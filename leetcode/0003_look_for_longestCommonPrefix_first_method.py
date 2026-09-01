class Solution:
    def longestCommonPrefix(self, strs):
        min_length = len(strs[0]) # 以第一个字符串作为标准参照
        target = 0 # 以第一个字符串索引下标作为标准参照
        for i in range(len(strs)): # 寻找长度最短的字符串，记录其对应的索引下标
            if len(strs[i]) < min_length:
                min_length = len(strs[i])
                target = i
        end = min_length-1 # 记录最长公共长缀的最后一个字母的下标
        for i in range(len(strs)):
            for j in range(min_length):
                if strs[i][j] != strs[target][j]:
                    if j-1 < end: # 更新最后一个字母的下标
                        end = j-1
        return strs[target][0:end+1] # 对字符串进行切片操作