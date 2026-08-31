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
