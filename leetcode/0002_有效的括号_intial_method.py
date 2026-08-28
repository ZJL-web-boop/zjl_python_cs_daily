class Solution(object):
    def isValid(self, s):
        dic={"[" : "]", "{" : "}", "(" : ")"}
        l = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                l.append(c)
            else:
                if not l:
                    return False
                last = l.pop()
                if c != dic[last]:
                    return False
        return len(l) == 0