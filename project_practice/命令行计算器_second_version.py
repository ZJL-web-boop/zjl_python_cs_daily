# 命令行计算器设计

"""
第二版主要优化的点有：
1. operation_table最好不用集合来表示，因为集合是无序的，这里我们换用列表；
2. 新增加了对于非法输入的数字的处理，如对"abc"的处理
"""
import time
operation_table = ['+', '-', '*', '/'] # 可以进行的计算操作，替换为有序的列表
print("计算器已打开")
time.sleep(1)
print("可以进行的计算操作有：",operation_table)
time.sleep(1)
print("请注意被减数或被除数要以第一个数字输入！")# 注意事项
print("请注意本计算器不支持小数参与的计算！")
time.sleep(1)
s1 = input("请输入您要参与计算的第一个数字：")
while not s1.isdigit(): # 当输入的数字不是合法的数字时（但是注意负整数也会进入这循环）
    # if s1[0] == '-' and s1[1:].isdigit(): # 当输入的是负整数时应为合法输入，跳出循环;注意这里有个bug:
    # 当输入的是空字符串的话，这里会出现IndexError（越界访问）
    if s1.startswith('-') and s1[1:].isdigit(): # 处理了越界的bug
        break
    print("请注意您输入的不是正确的数字表达！")
    s1 = input("请重新输入您要参与计算的第一个数字：")
num1 = int(s1)
s2 = input("请输入第二个数字：")
while not s2.isdigit():
    if s2.startswith('-') and s2[1:].isdigit():
        break
    print("请注意您输入的不是正确的数字表达！")
    s2 = input("请重新输入您要参与计算的第二个数字：")
num2 = int(s2)
operation = input("请输入您要进行的计算操作：")
while operation not in operation_table: # 非法操作输入的处理
    print("您输入的操作有误！")
    operation = input("请再次输入您要进行的计算操作：")
if operation == '+':
    print("结果是：",num1 + num2)
elif operation == '-':
    print("结果是：",num1 - num2)
elif operation == '*':
    print("结果是：",num1 * num2)
else:
    while num2 == 0: # 除数为0的处理
        print("请注意除数不能为0！")
        s2 = input("请再次输入第二个数字：")
        while not s2.isdigit():
            if s2.startswith('-') and s2[1:].isdigit():
                break
            print("请注意您输入的不是正确的数字表达！")
            s2 = input("请重新输入您要参与计算的第二个数字：")
        num2 = int(s2)
    print("结果是：",num1 / num2)