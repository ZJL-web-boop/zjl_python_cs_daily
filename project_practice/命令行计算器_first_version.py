# 命令行计算器设计

import time
operation_table = {'+', '-', '*', '/'} # 可以进行的计算操作
print("计算器已打开")
time.sleep(1)
print("可以进行的计算操作有：",operation_table)
time.sleep(1)
print("请注意被减数或被除数要以第一个数字输入！") # 注意事项
time.sleep(1)
num1 = int(input("请输入您要参与计算的第一个数字："))
num2 = int(input("请输入第二个数字："))
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
        num2 = int(input("请再次输入第二个数字："))
    print("结果是：",num1 / num2)