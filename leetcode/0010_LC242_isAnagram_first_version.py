class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): # 如果两个字符串的长度不相等，那肯定不是字母异位词（提前收工）
            return False
        dic = {}
        for c in s: # 构建一个哈希表，记录字符串s中的字符(key)和其对应的数量(value)
            dic[c] = dic.get(c,0) + 1
        for c in t:
            if c not in dic: # 如果t中的某字符不在s，那这二者必定不是字母异位词
                return False
            dic[c] -= 1 # 库存减1
        for c in dic: # 如果是字母异位词的话，最后字典中各字符的数量应该均为0
            if dic[c] != 0:
                return False
        return True