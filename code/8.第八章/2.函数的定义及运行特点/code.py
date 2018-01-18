# 如何定义一个函数
# 1.参数列表可以没有
# 2. return value None
@staticmethod
def funcname(parameter_list):
    pass


# 1.实现两个数的相加
# 2.打印输入的参数

def add(x,y):
    result = x +y
    return result

def print_code(code):
    print(code)

## 自定义函数名不要和系统函数名相同


## 设置递归的最大次数

import sys
sys.setrecursionlimit(1000000)

# 函数调用
add(1,2)
print_code('python')


# 函数的调用顺序
a = add(1,2)
b = print_code('python')
print(a,b)

