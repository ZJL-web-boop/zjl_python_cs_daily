"""第一版主要是使用列表与字符串之间的转换、
整数数组和字符串数组之间的转换解决这一问题
"""
class Solution(object):
    def plusOne(self,digits):
        s_digits = [str(x) for x in digits] # 首先先把整数数组转化为字符串数组，因为后续使用的.join函数只能接受字符串元素
        num = int(''.join(s_digits)) # 把字符串数组先变成字符串，再强制类型转换变成整数
        new_digits = list(str(num + 1)) # 整数先加1，然后变为字符串，最终转化为列表（即字符串数组）
        return [int(i) for i in new_digits] # 把字符串数组转变为整数数组