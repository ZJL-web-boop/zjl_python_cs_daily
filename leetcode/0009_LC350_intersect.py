class Solution(object):
    def intersect(self, nums1, nums2):
        nums3 = [] # 用来存放交集元素
        dic = {} # 构架一个哈希表来记录其中一个数组中的元素和其对应的数量，注意元素为key，对应的数量value
        for i in nums1: # 构建记录nums1中的元素和其对应的数量哈希表
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in nums2:
            if i in dic: # 如果i在表中，说明是交集元素
                if dic.get(i,0) > 0: # get函数会返回i对应的value值
                    nums3.append(i) # 元素进入列表，此操作的时间复杂度为O(1)
                    dic[i] -= 1 # 库存减1
        return nums3
