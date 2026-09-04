# 求和函数sum的知识点

## sum函数的几个常用参数：sum(iterable,start)

- iterable:我们一般自己要写的就是这个参数，它可以是任何可迭代对象——list、tuple、set、range、生成器都行；

```python  # 下面两行的结果都是 1+2+3
print(sum([1,2,3]))
print(sum(range(4)))
```

- start:一般来说，start = 0, 它是累加的初始值；

```python # 下面一行的结果都是 1+1+2+3
print(sum([1,2,3],start =1))
```