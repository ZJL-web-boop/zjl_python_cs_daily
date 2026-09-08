"""
题目说如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的，
同时要注意每个出现的字符都应当映射到一个字符（允许映射到自己），同时不改变字符的顺序，
不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身（只能是一对一的关系）。
正是因为只能是一对一的映射关系，所以只考虑由 s → t的做法是有问题的：
比如 s="badc"，t="baea",这个输入是能满足s → t的映射的，但是显然字符a和c都映射为a，不满足题意。
所以题目的要求应该为s → t和t → s的映射都要满足，上面例子显然不满足后者。

时间复杂度：O(n)（n为字符串的长度）
空间复杂度：O(n)
"""
# 题目已经声明两字符串的长度是一样的，均大于等于1

class Solution(object):
    def isIsomorphic(self, s, t):
        match1 = {} # 构建一个带值的哈希表来记录映射关系
        for i,m in enumerate(s): # 同时取出索引i和对应字符m
            if m not in match1: # 如果哈希表里面原来没有这个key,构建这一映射关系
                match1[m] = t[i]
            else: # 哈希表里面已经建立了这一映射关系
                if match1[m] != t[i]: # 检验映射是否正确
                    return False
        match2 = {} # 注意反向映射一定也要来一遍，否则可能不满足一一映射的条件
        for i,m in enumerate(t):
            if m not in match2: # 如果哈希表里面原来没有这个key,构建这一映射关系
                match2[m] = s[i]
            else: # 哈希表里面已经建立了这一映射关系
                if match2[m] != s[i]: # 检验映射是否正确
                    return False
        return True
