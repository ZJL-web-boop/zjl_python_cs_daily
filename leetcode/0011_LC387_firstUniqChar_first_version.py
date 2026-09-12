class Solution(object):
    def firstUniqChar(self, s):
        dic = {}
        for c in s: # 构建哈希表：s中的字符为key，对应的数量为value（注意这个过程是按照字符串中字符出现的先后顺序构建的）
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        for i, v in dic.items(): # 在字典中查询第一个对应value值为1的元素
            if v == 1:
                return s.find(i)  # 找到指定元素，返回对应的索引下标
        return -1 # 字符串中没有唯一的元素

# 注意这种方法是有语言限制的，在Python 3.7 之前dict是无序的，在构建哈希表时就无法保证原有字符出现的先后顺序
