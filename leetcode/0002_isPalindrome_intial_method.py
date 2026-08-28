class Solution(object) :
    def isPalindrome(self, s):
        if s < 0 :
            return False
        elif 0 <= s < 10:
            return True
        else :
            s1 = 0
            s2 = s
            while s > 0 :
                s1 = s1 * 10 + s % 10
                s //= 10
            if s1 == s2 :
                return True
            return False