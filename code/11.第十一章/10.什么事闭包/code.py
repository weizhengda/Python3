# 闭包 = 函数 + 环境变量
def curve_pre():
    a = 25
    def curve(x):
        y = a*x*x
    return curve

a = 10
f = curve_pre()
print(f(2))