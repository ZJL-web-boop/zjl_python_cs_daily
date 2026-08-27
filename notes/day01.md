# Day 1--leetcode 1:两数之和

## 题目
给定一个列表和目标值，寻找列表中是否有两个数之和为target,若存在，
则返回相应的下标。

## 解法一：暴力两层循环求解
当我们每次遍历到一个值x(相应下标为i)时，我们应该接着进行第二层遍历，
即对x后面的值进行遍历，看其中有没有等于 target-x 的值，有则返回对应两个下标。

时间复杂度：O(n²)，需要下一步优化；

缺点：进行了两次遍历，优化想法：能不能把第二次遍历变成一个时间复杂度为O(1)的操作（利用哈希表查询）

代码：

    class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return None

## 优化解法：利用哈希表（python中为字典）进行O(1)的查询操作
算法思路：当我们第一次遍历到一个下标为i,值为x的项时，我们直接去字典（key为值，value为对应的下标）中查询是否有key等于
target-x 的项，若有则返回对应的两个下标，否则把这一项加到字典中继续往后遍历；

时间复杂度分析：算法本质上只是遍历了一次，时间复杂度为O(n)，效率较高；

注意事项：1、字典的 key和value 对应的含义不要搞反了，目标是返回下标，所以key应为值，value为对应的下标；
        2、不能先遍历完再查询，因为这可能会出现自身和自身相加为target的情况：比如 nums=[3,2,4],target=6 这个输入；

代码：
    
    class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i,x in enumerate(nums):
            if target-x in d:
                return [d[target-x],i]
            d[x]=i
        return None

## 收获
使用字典进行查询操作可以实现O(1)的时间复杂度，这一思想在两数相加、去重、计数等系列有所应用。


# 2026/8/27 大模型学习第一天
一、 廖雪峰教程：python学习笔记

1、 python 是解释型语言，程序执行时是边编译边运行，运行速度比较慢；而C语言是编译型语言，是先把所有东西编译为CPU能看懂的机器码，然后再运行，运行速度比较快；

2、list 学习：

- 求列表长度：len(list);

- 如果要从后面开始取，则可以用索引-1，-2等等；

- 尾部添加函数：list.append("");

- 固定位置添加函数：list.insert(索引，添加的值)（原索引位置添加新元素，原先的元素往后推）；

- 删除尾部的元素：list.pop()，删除特定位置的元素：list.pop(索引)；

- list中的元素类型也可以不同，并且list可以相互嵌套；

3、字典dictionary学习：

- 如何避免key不存在：

    方法一：执行 key in dict 操作，看返回的是True 还是 False;

    方法二：用 get 操作，d.get(key) / d.get(key,自己写的值)，如果key存在，则返回对应的value;
如果key不存在，则返回None或自己写的值。

- 删除key 的操作：dict.pop(key), 对应的value 也会被删除；

- 注意dict中的key是不可变对象，相同的key 必须得出相同的结果，字符串、整数等是不可变的，而list是可变的；