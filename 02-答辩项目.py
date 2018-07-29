list = []

account = "123"
password = "123456"

def add():
    haoyou = {}
    name = input("请输入好友姓名:")
    haoyou["name"] = name
    account1 = int(input("请输入好友账号:"))
    haoyou["account1"] = account1
    list.append(haoyou)
    print("添加成功")

def find():
    name = input("请输入要查找的姓名:")
    for haoyou in list:
        if haoyou["name"] == name:
            print("好友姓名%s\n好友账号%d"%(haoyou["name"],haoyou["account1"]))
            break



def delete():
    name = input("请输入要删除好友的姓名:")
    for haoyou in list:
        if haoyou["name"] == name:
            list.remove(haoyou)
            print("删除成功")
            break

def print_list():
    print("姓名    账号")
    for haoyou in list:
        print("%s    %d"%(haoyou["name"],haoyou["account1"]))








def print_menu():
    print("请登录微信:")
    while True:
        acc = input('请输入账号:')
        pwd = input('请输入密码:')
        if account == acc and password == pwd:
            print("登录成功")
            choose()
        else:
            print("请重新登录")
            break


def choose():
    print("请选择功能:".center(30," "))
    while True:
        print("1、添加")
        print("2、查找")
        print("3、删除")
        print("4、列表")
        print("5、退出登录")
        print_info()

def print_info():
    num = int(input("请选择功能:"))
    if num == 1:
        add()#调用添加
    elif num == 2:
        find()#调用查找
    elif num == 3:
        delete()
    elif num == 4:
        print_list()
    elif num == 5:
        exit()
print_menu() 






