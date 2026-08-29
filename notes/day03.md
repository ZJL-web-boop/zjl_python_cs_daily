# Day 3 - LeetCode 13. 罗马数字转整数

# 一 、LeetCode 13. 罗马数字转整数

## 题目

罗马数字包含以下七种字符: I， V， X， L，C，D 和 M，给定一个罗马数字，我们把它转化为整数。

    字符          数值
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

## 解法 ：直接从左到右遍历字符串，遇到啥加其对应的整数（一般情况）

思路：一般来说，罗马数字中数字小的在数字大的右边，所以我们直接从左到右遍历字符串，遇到啥加其对应的整数。但是只存在以下特例：

    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

所以针对这些情况，我们可以在遍历到I、X、C时，在保证不越界的前提下检查它们后面的字母，如果分别对应的是V和X、L和C、D和M，

则把它们原先对应的正整数分别换为其相反数，比如 I: 1 变为 -1。

- 时间复杂度：O(n) （n为字母的个数）

代码：
```python
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
```

### 可以优化的小点

为了把代码简化，我们可以把罗马数字和其对应的整数制作成哈希表（即字典），即

```python
dic = {'I' : 1, 'V' : 5, 'X' : 10} # 这里只展示一部分
```

由于本质思路没变，这里就不修改代码了

### 易踩坑点

在处理特殊情况时，一定要注意是否会越界访问的问题！！！