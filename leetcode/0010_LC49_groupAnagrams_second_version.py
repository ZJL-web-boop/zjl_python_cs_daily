class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        for word in strs:
            key = tuple(sorted(word)) # 排序后异位词的key完全相同（列表不可哈希，要转成元组）
            if key in dic:
                dic[key].append(word)
            else:
                dic[key] = [word]
        return list(dic.values())