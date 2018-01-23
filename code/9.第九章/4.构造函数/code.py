
# 模板
clss Student():
    name = ''
    age = 0

    def __init__(self,name,age):
        # 构造函数
        # 初始化对象的属性
        name = name
        age = age
        # print('student')

    # 行为特征
    def do_homework(self):
        print('homework')
    
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)


student1 = Student('石敢当',18)
student1.plus_sum()