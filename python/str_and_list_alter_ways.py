# 字符串 → 列表
s = "hello world"
list(s)        # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']  拆成字符，空格也在
s.split()      # ['hello', 'world']                                       按空白拆成单词
s.split('l')   # ['he', '', 'o wor', 'd']                                 按指定字符拆

# 列表 → 字符串 但需要注意的是join函数只能处理字符串数组
lst = ['hello', 'world']
' '.join(lst)   # 'hello world'   用空格拼
'-'.join(lst)   # 'hello-world'   用连字符拼
''.join(lst)    # 'helloworld'    直接拼（常用！）
