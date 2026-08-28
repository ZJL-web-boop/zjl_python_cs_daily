class Solution(object):
    def isPalindrome(self, s):
        s1=str(s)
        return s1 == s1[::-1]  # 切片反转，切片得到的是字符串