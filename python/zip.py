# zip函数知识点

print(zip('abc', [1, 2, 3]))
print(list(zip('abc', [1, 2, 3])))
# [('a', 1), ('b', 2), ('c', 3)]  —— 每一对都是一个元组

"""
注意第一件事：zip(...) 本身返回的是迭代器（惰性对象），直接 print 只会看到 <zip object at ...>,
要用 list() 等包一层才看得到内容。
"""

# 三个常用场景
# 1. 配对遍历（最常用，比你手动 range(len) 优雅）
for c1, c2 in zip('badc', 'baba'):
    print(c1, c2)          # b b / a a / d b / c a

# 2. 一行解包还原（* 把列表摊开成多个参数）
pairs = [('a', 1), ('b', 2)]
s, t = zip(*pairs) # s = ('a','b'), t = (1,2)  —— 注意得到的是元组
print(s, t)

# 3. 造字典（dict 要吃成对数据，zip 现成供给）
print(dict(zip('abc', [1, 2, 3])))  # {'a': 1, 'b': 2, 'c': 3}

# 注意zip是按最短的截断的

print(list(zip('abc', '12')))
# [('a', '1'), ('b', '2')]  —— c 被悄悄丢掉了，zip 不报错


