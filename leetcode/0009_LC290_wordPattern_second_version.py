"""
第二版使用zip()函数和集合解决这一问题
"""

class Solution(object):
    def wordPattern(self, pattern, s):
        s_list = s.split() # 由于s中是一个个由单空格符分隔的单词，为了更好的直接用索引访问单词，这里我们把s转换为列表
        if len(s_list) != len(pattern):
            # 如果长度不相等的话，那一对一的映射关系必然不成立（“提前收工”）
            # 注意由于zip函数是按最短的截断“拉链”的，所以这判断就不能省了，因为可能出现像'ab'，'dog cat cat'的情况
            return False
        return len(set(zip(pattern, s_list))) == len(set(pattern)) == len(set(s_list))