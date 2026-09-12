print('abcebca'.strip('abc')) # 输出'e'，注意这里不一定是要按abc的顺序消除，只要是遇到abc即可，如果遇到其他字符就停止
print('aebcebca'.strip('abc')) # 输出'ebce'