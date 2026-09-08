"""
题目问字符串ransomNote能否由字符串magazine里面的字符构成（magazine中的每个字符只能在 ransomNote中使用一次），能则返回True。
那不能构成的情况就是：
 要么在ransomNote中存在的字符，在magazine里面不存在；
 要么在ransomNote中存在的字符，虽然magazine里面也有，但是没ransomNote里数量更多；
那么我们就既需要对字符进行查询操作，又要对同一种字符进行数量的比较操作，所以我们采用字典的结构解决这一问题。

时间复杂度：O(n)（n为ransomNote 和 magazine长度的较大值）
空间复杂度：O(n)（n为magazine长度）
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # 这里其实可以先进行一个前置的判断：如果ransomNote的长度大于magazine的长度，则必返回False（提前收工）
        if len(ransomNote) > len(magazine):
            return False
        stock = {} # 以字符为key，以对应的数量为value
        for c in magazine:
            stock[c] = stock.get(c, 0) + 1
            # 注意这里的get函数的参数含义：如果本次操作前c在字典中已经存在，则返回对应的value值，不存在则返回0.
        for i in ransomNote:
            if i not in stock: # 在ransomNote中存在的字符，在magazine里面不存在
                return False
            if stock[i] == 0: # 先判断stock里面是否还有i字符，没有的话就返回False
                return False
            stock[i] -= 1 # 用了一个就库存就减1
        return True