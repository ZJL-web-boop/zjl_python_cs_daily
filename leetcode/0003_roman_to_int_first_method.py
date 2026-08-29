class Solution(object):
    def romanToInt(self,s):
        num = 0
        length = len(s)
        for i in range(length):
            if s[i] == 'I':
                if (i+1) < length:
                    if s[i+1] == 'V' or s[i+1] == 'X':
                        num -= 1
                    else:
                        num += 1
                else:
                    num += 1
            elif s[i] == 'V':
                num += 5
            elif s[i] == 'X':
                if (i+1) < length:
                    if s[i+1] == 'L' or s[i+1] == 'C':
                        num -= 10
                    else:
                        num += 10
                else:
                    num += 10
            elif s[i] == 'L':
                num += 50
            elif s[i] == 'C':
                if (i+1) < length:
                    if s[i+1] == 'D' or s[i+1] == 'M':
                        num -= 100
                    else:
                        num += 100
                else:
                    num += 100
            elif s[i] == 'D':
                num += 500
            else:
                num += 1000
        return num