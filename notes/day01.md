# Day 1 — LeetCode 1. 两数之和（2026/8/27）

## 题目

给定一个整数列表 nums 和目标值 target，找出列表中是否存在两个数之和为 target，若存在，返回它们的下标。

## 解法一：暴力两层循环

思路：每遍历到一个值 x（下标 i）时，再对 x 之后的元素做第二层遍历，看有没有等于 target - x 的值，有则返回两个下标。

- 时间复杂度：O(n²)
- 空间复杂度：O(1)
- 缺点：第二层遍历是 O(n) 的回头扫，需要优化

优化方向：能不能把"找 target - x"这个动作变成 O(1)？——利用哈希表查询。

```python
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
```

## 解法二：哈希表（字典）边查边存

思路：遍历到下标 i、值为 x 时，先查字典里有没有 key 等于 target - x：
- 有 → 直接返回 [字典里存的下标, i]
- 没有 → 把 (x → i) 存入字典，继续往后走

- 时间复杂度：O(n)，只遍历一次
- 空间复杂度：O(n)，字典最多存 n 个元素

```python
class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, x in enumerate(nums):
            if target - x in d:
                return [d[target - x], i]
            d[x] = i
        return None
```

### 注意事项

1. 字典的 key / value 含义不要搞反：目标是返回下标，所以 **key 为值，value 为下标**（字典是拿 key 查 value 的）
2. 必须**边查边存**，不能先全部存完再查，否则会出现"自己配自己"：如 nums=[3,2,4], target=6，全存后查到 target-3=3 是自己，错误返回 [0,0]
   - 键覆盖问题：nums=[3,3] 时，先全存会导致 d[3]=0 被 d[3]=1 覆盖

## 收获

- 字典查询是 O(1)，是"空间换时间"的经典套路，在两数之和、去重、计数等系列问题中反复出现
- `enumerate(nums)` 可以同时拿到下标和值

## 待复习

- [ ] 排序 + 双指针能否解这题？为什么这题一般不用？（提示：排序会打乱下标）
- [ ] 闭卷复述：能否 5 分钟内不看资料写出哈希解法

---

# 2026/8/27 廖雪峰 Python 笔记

1. Python 是解释型语言，边解释边运行，速度较慢；C 是编译型语言，先编译成机器码再运行，速度快。

2. list：

- 求长度：`len(lst)`
- 从后往前取：索引 `-1`、`-2`
- 尾部添加：`lst.append(x)`
- 指定位置添加：`lst.insert(索引, 值)`，原位置元素后移
- 删除：`lst.pop()` 删尾部并返回；`lst.pop(索引)` 删指定位置
- 元素类型可以不同，list 可嵌套

3. dict：

- 判断 key 是否存在：`key in d` 返回 True/False
- 安全取值：`d.get(key)` 不存在返回 None；`d.get(key, 默认值)` 不存在返回默认值
- 删除：`d.pop(key)` 连同 value 一起删除
- key 必须是不可变对象（字符串、整数可以；list 不行）
