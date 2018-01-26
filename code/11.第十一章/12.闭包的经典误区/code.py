def f1():
    a = 10
    def f2():
        # a 会被python认为是一个局部变量
        return a
    return f2
        #print(a) 
   # print(a) #10
   # f2() #20
   # print(a) #10

f = f1()
print(f)
print(f._closure_)