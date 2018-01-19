
# 面向对象
# 有意义的面向对象的代码

# 类 = 面向对象
# 类、对象
# 实例化
# 类最基本的作用：封装

class Student():
    name = '' 
    age = 0

    def print_file(self):
        print('name: ' +self.name)
        print('age: ' + str(self.age))
        
class StudentHomework():
    homework_name = ''
      
student = Student()
student.print_file()
