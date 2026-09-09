name = 'Zhang Jiale'
print(name.find('ang')) # 输出a的下标：2
print(name.find('y')) # 查找失败，返回-1
print(name.find('ang', 2, 4)) # 由于查找区间是包前不包后的，所以'g'不在该区间内，查找失败输出：-1
print(name.find('ang', 2, 5)) # 输出：2
print(name.find('a', 3)) # 输出：8，结束位置没写意味着一直到最后
print(name.find('a', 2)) # 输出：2