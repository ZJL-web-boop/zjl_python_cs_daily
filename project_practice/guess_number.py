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
if count > 7 or (count ==7 and number != answer):
    print("很遗憾！您的猜测次数已用完!")
    print('挑战失败！')
else:
    print('恭喜您猜测成功！')
    print(f'总共用了{count}次猜对')
