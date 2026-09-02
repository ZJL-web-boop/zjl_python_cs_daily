"""第三版主要是采用对列表内的各元素从右往左进行逐位进位的操作
"""

class Solution(object):
    def plusOne(self,digits):
        i = len(digits)-1 # 最后一个索引下标
        if digits[i] < 9: # 不需要进位操作
            digits[i] += 1
            return digits
        while i>=0 and digits[i]==9: # 末位为9的情况
            digits[i] = 0
            if i == 0: # 比如把[9]变成[10]，要向表头新增一个1
                digits.insert(0,1)
                break
            elif digits[i-1] < 9: # 不需要进位操作
                digits[i-1] += 1
                break
            else: #索引为i-1的项值为9且i > 0，现在我们要对这项之前的项进行加1操作
                i = i-1
        return digits