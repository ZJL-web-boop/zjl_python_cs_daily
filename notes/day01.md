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