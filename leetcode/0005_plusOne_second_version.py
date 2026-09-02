"""第二版主要是使用了递归的思路解决这一问题
"""

class Solution(object):
    def plusOne(self, digits):
        length = len(digits) # 记录整数数组的长度
        if not digits: # 列表为空时
            return [1]
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else: # 列表最后一个元素为9，大整数+1后末位变为0，剩余部分的变化我们可以视为：对原来去掉最后一位的新整数加1的操作
            lis = digits[:]
            lis.pop()
            return self.plusOne(lis) + [0] # 递归调用
