# Day 4 - 猜数字游戏设计

## 题目

我们现在要用python设计出传统的猜数字游戏，并规定最多可猜测的次数（本样例规定为7次），猜测的数字不在规定范围内
、大了或小了都会给出相关提示，当猜对时也会显示出使用的次数。

## 解法：使用输入输出、循环、条件判断等实现猜数字游戏

思路：这道题的思路其实不难，使用了input、print、while循环、if/else等条件判断实现了这一功能，这里便不详细阐述了。

代码：（这里提供两版代码，第二版是在第一版的基础上改进的）
```python
# 1-100 猜数字游戏设计

import random
import time
count=0 # 记录用户猜测次数
print('猜数字游戏现在开始!')
time.sleep(1.5)
print('请注意数字的范围在1-100之间（含1和100）')
time.sleep(1.5)
print('您要注意您的猜测次数最多为7次！')
time.sleep(1.5)
random.seed(0)  # 固定一个随机数，便于用户猜测
answer = random.randint(1,100) # 注意含1和100
number =  int(input('请输入您要猜测的数字：'))
time.sleep(1)
if number == answer:
    count = count + 1
while number != answer and count <7:
    if number > answer:
        if number > 100:
            print('您猜的数不在规定范围内，请重新猜测!')
            time.sleep(1)
        else:
            print('您猜的数大了！请重新猜测!')
            time.sleep(1)
        count += 1
        if count < 7:
            print("请注意您的猜测次数剩余",7-count,'次')
            time.sleep(1)
            number =  int(input('请输入一个更小的数字：'))
            time.sleep(1)
            if number == answer:
                count = count + 1
    else:
        if number < 1:
            print('您猜的数不在规定范围内，请重新猜测!')
            time.sleep(1)
        else:
            print('您猜的数小了！请重新猜测!')
            time.sleep(1)
        count += 1
        if count < 7:
            print("请注意您的猜测次数剩余",7-count,'次')
            time.sleep(1)
            number = int(input('请输入一个更大的数字：'))
            time.sleep(1)
            if number == answer:
                count = count + 1
if count ==7 and number != answer:
    print("很遗憾！您的猜测次数已用完!")
    print('挑战失败！')
else:
    print('恭喜您猜测成功！')
    print(f'总共用了{count}次猜对')

```

```python
# 猜数字游戏设计

""" 本次优化主要是针对off-by-one（在day04总结中会阐释这个概念）问题进行
"""

import random
import time
random.seed(0)  # 固定一个随机数，但不一定是0
answer = random.randint(1, 100) # 注意这是包含1和100的
max_count = 7 # 规定最多可尝试7次
count = 0 # 用来记录一共尝试了几次，要跟用户输入了几次一致
print("猜数字游戏现在开始！")
time.sleep(1.5) # 设定1.5秒的时间间隔，防止相邻两次与用户的交互的间隔时间非常短导致效果不佳，保证用户有一定的缓冲时间
print("请注意数字的范围为1到100（含1和100）")
time.sleep(1.5)
print("请注意您最多只能猜测7次，请慎重考虑！")
time.sleep(1.5)
while count < max_count: # 当猜测次数少于7次时进入循环，由于count为6时能进入循环，所以最多猜测次数为7
    number = int(input('请输入您要猜测的数字：'))
    count += 1 # 每输入一次count加一，从而保证了猜测次数的准确性，避免了off-by-one的情况出现
    if number > 100 or number < 1: # 检验输入的合法性
        print("您输入的数字不在规定范围内，请重新输入！")
    elif number == answer:
        print("恭喜您挑战成功！")
        time.sleep(1.5)
        print(f'您一共用了{count}次答对')
        break  # 猜测猜对时则退出循环
    elif number > answer:
        print('您输入的数大了，请输入一个更小的数！')
    else:
        print('您输入的数小了，请输入一个更大的数！')
    print(f'请注意您的剩余猜测次数为{max_count-count}次！')
    if count == max_count: #由于答对必会在上面退出循环，所以执行到这一步肯定就是用完了7次机会且没有答对的结果
        print('很遗憾！您未能在规定次数内成功猜测，请重新挑战！')
```

### off-by-one 问题

off-by-one问题，即差异错误：结果总是比正确的多一或少一（循环和计数里最常见的坑），这一错误经常出现在以下三类场景中：

- 循环结束条件写错：比如 > 写成 >=
- 数组下标搞错：从0开始错认为是从1开始
- 计数 count 加1的时机搞错：计数的时机搞错

### 第二个版本相比与第一个版本优化的点：

第一个版本是可行的，但是它的计数点分布有点杂、有点混乱了；

相比之下，第二个版本的计数逻辑就比较清晰了：每输入一次计数加1，避免了off-by-one问题的出现。

另外，第二版检验输入合法性的操作合并了，这样的好处是比如如果以后要修改数字的范围只需要修改random.randint和此处即可,
不需要修改多处。

## 收获
深刻理解了off-by-one错误以及它出现的原因，厘清了本题的计数逻辑。

## 待复习

现在输入 150 也会消耗一次机会。如果设计改成“非法输入不消耗次数”，count += 1 应该挪到哪里？