class Solution(object):
    def firstUniqChar(self, s):
        dic = {}
        for c in s: # 构建哈希表：s中的字符为key，对应的数量为value
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        for i, c in enumerate(s): # 按照字符串原先的顺序从左到右遍历，不需要考虑字典有没有序的问题（解决了版本1的语言限制问题）
            if dic[c] == 1:
                return i
        return -1 # 字符串中没有唯一的元素