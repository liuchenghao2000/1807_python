class Manger():
    def __inir__(self):
        self.name = '学生管理大师v1.0'
        self.list = []

    def add(self,stu):
        self.list.append(stu)
        self.writerizhi('几点掉了add方法')

    def find(self):
        self.writerizhi('几点掉了find方法')
        pass

    def delete(self):
        pass

    def change(self):
        pass

    def writerizhi(self,str):
        '''
        写文件
        '''

class Student():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    m = Manger()
    while True:
        name = input('请输入学生姓名：')
        age = input('请输入学生年龄：')
        sex = input('请输入学生性别：')
        stu = Student(name,age,sex)
        m.add(stu)
