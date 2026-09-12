class Solution(object):
    def intersection(self, nums1, nums2):
        dic = {}
        for num in nums1: # 构建一个哈希表：nums1中的元素为key，其对应的数量为value
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        lis = [] # 用来存放最后的交集元素
        for num in nums2:
            if dic.get(num, 0) > 0: # 如果num是二者共有的，且是第一次在循环遍历中出现，才能满足这个判定条件
                lis.append(num)
                dic[num] = 0 # 确保相同的元素只存一个，只要第一个存了，就清空库存
        return lis