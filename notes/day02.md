# Day 1--leetcode 2: 回文数

## 题目
回文数是指按照正序和逆序读是一样的整数，比如说121是回文数，而-121就不是回文数；

现在要求给定一个整数x，我们要判断其是否是回文数；

## 解法一：采用入栈出栈的思路把一个整数逆转，看其是否和原数一样
算法思路：首先我们能够判断负数一定不是回文数，个位数一定是回文数，这两种情况我们可以优先判断；

当x是比9大的数时，我们可以让它从个位开始先入栈，然后依次出栈，利用栈先入后出的特点我们可以得到逆转后的数，判断其是否和原数一样。

代码：
    
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

学到的 python 知识点：

1、与C语言不同，python 中的逻辑运算符为 and、or;

2、python 中是支持这种 0 <= s < 10 链式写法，比 s >= 0 and s < 10 更地道；

3、在C中 s /= 10 为 s整除10,但 python 中计算出来是浮点数，应用 // 整除符号；

## 解法二: 将整数转化为字符串
算法思路：先把整数转化为字符串，然后看它和它的反向切片是否相等；

代码：

    class Solution(object):
    def isPalindrome(self, s):
        s1=str(s)
        return s1 == s1[::-1]  # 切片反转，切片得到的是字符串

