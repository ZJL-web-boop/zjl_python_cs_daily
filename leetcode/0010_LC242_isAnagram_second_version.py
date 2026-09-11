class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): # 如果两个字符串的长度不相等，那肯定不是字母异位词（提前收工）
            return False
        dic = {}
        for c in s: # 构建一个哈希表，记录字符串s中的字符(key)和其对应的数量(value)
            dic[c] = dic.get(c,0) + 1
        for c in t:
            if dic.get(c,0) == 0:
                """
                如果t中的某字符不在s中，那二者必不是字母异位词；
                如果t中的字符全在s中出现过，由于二者长度一致，但凡t里某个字符多提一次，就会在那一刻撞到库存0；
                而如果一次都没撞到，n 次提货恰好耗尽 n 个库存，必然全 0     
                """
                return False
            dic[c] -= 1 # 库存减1
        return True