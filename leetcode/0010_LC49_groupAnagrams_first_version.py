from string import ascii_lowercase # 导入含26个字母（按顺序）的字符串
class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        for word in strs: # 构建26字母的数量元组作为键值、对应的字符异位词列表作为value的哈希表
            key = tuple(word.count(c) for c in ascii_lowercase)
            if key in dic:
                dic[key].append(word)
            else:
                dic[key] = [word]
        return list(dic.values()) # 取字典中的value值（小列表）合并为一个大列表