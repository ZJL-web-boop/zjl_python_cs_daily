# Day 5 - LeetCode 14. 最长公共前缀

## 题目

查找字符串数组中的最长公共前缀，若无公共前缀，则返回''。比如，

- 输入：strs = ["flower","flow","flight"]
- 输出："fl"

## 解法：通过循环遍历字符串和字符之间的比较进行解答

思路：首先我们容易得出最长公共前缀一定是属于数组中最短的字符串，所以我们可以先得到最短字符串的索引下标以及它的长度，这样能省去一些不必要的
比较操作（比如较长字符串后面部分我们就可以不考虑了）。

然后我们就对各字符串进行遍历，不断更新公共前缀的下标，最终得到最长公共前缀。

- 时间复杂度：O(n×m)，其中n为数组中字符串的数量，m为最短字符串的长度。

代码：

```python
class Solution:
    def longestCommonPrefix(self, strs):
        min_length = len(strs[0]) # 以第一个字符串作为标准参照
        target = 0 # 以第一个字符串索引下标作为标准参照
        for i in range(len(strs)): # 寻找长度最短的字符串，记录其对应的索引下标
            if len(strs[i]) < min_length:
                min_length = len(strs[i])
                target = i
        end = min_length-1 # 记录最长公共长缀的最后一个字母的下标
        for i in range(len(strs)):
            for j in range(min_length):
                if strs[i][j] != strs[target][j]:
                    if j-1 < end: # 更新最后一个字母的下标
                        end = j-1
        return strs[target][0:end+1] # 对字符串进行切片操作
```

### 亮点

我这里并不是直接以第一个字符串作为哨兵去贯穿整个代码的，它只是作为参照帮我找到了最短的字符串，然后再以最短的字符串作为参照进行后续的操作，
这样能减少一些不必要的比较。

## 收获

开始的时候我是写

```python
min_length = 200 # 题目规定的字符串的最大长度
target = -1
```

但是这个写法是不规范的，我们习惯还是以第一个字符串作为哨兵去做参照。

## 待复习

能不能对以下部分再进行进一步的优化呢？（提示：这里的 j-1 < end 其实可以被优化，因为对于单个字符串的话，end = j-1 即可，
再往后遍历的话也不会触及到这一判断条件）

```python
        for i in range(len(strs)):
            for j in range(min_length):
                if strs[i][j] != strs[target][j]:
                    if j-1 < end: # 更新最后一个字母的下标
                        end = j-1
```