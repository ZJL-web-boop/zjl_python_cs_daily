""" 这次的改进主要是寻找六组特例之间的内在联系
然后用字典消除了单列特例的多层if else 嵌套
"""
class Solution(object):
    def romanToInt(self, s):
        dic = { 'I' : 1, 'V' : 5, 'X' : 10,
                'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}  # 哈希表（字典）的构建：罗马字母为key，其对应的整数为value
        total = 0 # 用total来记录最后的整数值
        for i in range(len(s)): # 这里要注意不能使用for c in s，因为后续要检验是否越界的问题
            if i+1 < len(s) and dic[s[i]] < dic[s[i+1]]: # 那六个特例的情况，且注意这里是先检验是否越界再进行访问操作
                total -= dic[s[i]]
            else:
                total += dic[s[i]]
        return total