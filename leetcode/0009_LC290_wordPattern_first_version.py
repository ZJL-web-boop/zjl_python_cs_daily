class Solution(object):
    def wordPattern(self, pattern, s):
        s_list = s.split() # 由于s中是一个个由单空格符分隔的单词，为了更好的直接用索引访问单词，这里我们把s转换为列表
        if len(s_list) != len(pattern): # 如果长度不相等的话，那一对一的映射关系必然不成立（“提前收工”），注意len()是O(1)的操作
            return False
        dic1 = {}
        for i, m in enumerate(pattern):
            if m not in dic1:
                dic1[m] = s_list[i]
            else:
                if dic1[m] != s_list[i]:
                    return False
        dic2 = {}
        for i, m in  enumerate(s_list):
            if m not in dic2:
                dic2[m] = pattern[i]
            else:
                if dic2[m] != pattern[i]:
                    return False
        return True
