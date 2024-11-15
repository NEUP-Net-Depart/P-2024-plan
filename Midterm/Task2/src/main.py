# 学生管理系统

# PS: 可以仅以 “姓名” / “学号” 来代指学生信息

import json
import queue

STU_LIST = []

def stu_init():
    """此函数用于, 从文件中, 初始化学生信息"""
    with open('Students.json', 'r', encoding='utf-8') as f:
        for row in json.load(f):
            STU_LIST.append(row)
            print(row)


def get_choice() -> int:
    """此函数用于, 在命令行里, 获取用户输入的选项"""
    while True:
        try:
            choice = int(input("请输入整数指令:"))
            return choice
        except ValueError:
            print("指令无效，请重新输入！")


def menu():
    """此函数用于, 在命令行里, 打印出菜单"""
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查询学生信息')
    print('5.保存学生信息')
    print('6.分班')
    print('7.待办事项')
    print('0.退出系统')


def exec():
    """此函数用于, 根据用户输入的选项, 执行相应的功能"""
    match user_choice:
        case 1:
            stu_add()
        case 2:
            stu_del()
        case 3:
            stu_mod()
        case 4:
            a = input('请输入要查询学生的学号：')
            stu_sel(a)
        case 5:
            stu_save()
        case 6:
            stu_set_class()
        case 7:
            stu_pending()


def stu_add():
    """此函数用于, 添加学生信息"""
    flag = True
    while flag:
        a = input("请输入姓名：")
        b = input("请输入学号：")
        c = input("请输入学院：")
        d = input("请输入专业：")
        e = input("请输入班级：")
        f = input("请输入绩点：")
        student = {
            '姓名': a,
            '学号': b,
            '学院': c,
            '专业': d,
            '班级': e,
            '绩点': f
        }
        STU_LIST.append(student)
        print("添加成功！")

        a = input('是否要继续添加y/n')
        while True:
            if a == 'y': break
            elif a == 'n':
                flag = False
                break
            else :
                 a = input('输入不合法，请重新输入：y/n')


def stu_del():
    """此函数用于, 删除学生信息"""
    running = True
    while running:
        flag = False
        dl = input('请输入要删除学生的学号：')
        for i in range(0,len(STU_LIST)):
            if STU_LIST[i].get('学号') == dl:
                STU_LIST.pop(i)
                flag = True
        if flag == False:print('该学生不存在！')
        else :print('删除成功！')

        a = input('是否要继续删除y/n')
        while True:
            if a == 'y': break
            elif a == 'n':
                running = False
                break
            else :
                 a = input('输入不合法，请重新输入：y/n')


def stu_mod():
    """此函数用于, 修改学生信息"""
    dl = eval(input("请输入要修改学生的学号："))
    index = stu_sel(dl)
    print('以下是可修改内容：')
    print('1.姓名')
    print('2.学号')
    print('3.学院')
    print('4.专业')
    print('5.班级')
    print('6.绩点')
    print('7.全部')
    order = eval(input('请输入指令：'))
    match order:
        case 1:
            STU_LIST[index]['姓名'] = input('请输入姓名：')
        case 2:
            STU_LIST[index]['学号'] = input('请输入学号：')
        case 3:
            STU_LIST[index]['学院'] = input('请输入学院：')
        case 4:
            STU_LIST[index]['专业'] = input('请输入专业：')
        case 5:
            STU_LIST[index]['班级'] = input('请输入班级：')
        case 6:
            STU_LIST[index]['绩点'] = input('请输入绩点：')
        case 7:
            STU_LIST[index]['姓名'] = input('请输入姓名：')
            STU_LIST[index]['学号'] = input('请输入学号：')
            STU_LIST[index]['学院'] = input('请输入学院：')
            STU_LIST[index]['专业'] = input('请输入专业：')
            STU_LIST[index]['班级'] = input('请输入班级：')
            STU_LIST[index]['绩点'] = input('请输入绩点：')


def stu_sel():
    """此函数用于, 查询学生信息"""
    flag = False
    for i in range(0,len(STU_LIST)):
        if STU_LIST[i].get('学号') == dl:
            print(STU_LIST[i])
            flag = True
            return i
    if flag == False: print('该生不存在！')


def stu_save():
    """此函数用于, 将学生信息保存到文件中"""
    with open('Students.json', 'w', encoding='utf-8') as f:
        json.dump(STU_LIST, f, ensure_ascii=False, indent=4)
    print('保存成功！')


def stu_sel_pure(dl):
    """此函数用于, 查询学生信息(纯享版)"""
    flag = False
    for i in range(0,len(STU_LIST)):
        if STU_LIST[i].get('学号') == dl:
            flag = True
            return i


def stu_set_class():
    lst = []  #存储所有学生信息
    #用于将STU_LIST的内容复制到lst中
    for i in range(0,len(STU_LIST)):
        lst1 = []
        lst1.append(STU_LIST[i]['学号'])
        lst1.append(STU_LIST[i]['专业']+STU_LIST[i]['班级'])
        lst.append(lst1)

    while len(lst):
        lst_class = []
        lst_class.append(lst[0])

        for j in range(1,len(lst)):
            if(set.intersection(set(lst[0]),set(lst[j]))):
                lst_class.append(lst[j])
                lst.pop(j)

        #要去掉专业班级
        with open('./Classes/' + lst[0][1] + '.json', 'w', encoding='utf-8') as f:
            if len(lst_class) == 1:
                for row in lst_class:
                    index = stu_sel_pure(row[0])
                    json.dump(STU_LIST[index], f, ensure_ascii=False, indent=4)
            else:
                lst_class1 = []
                for row in lst_class:
                    index = stu_sel_pure(row[0])
                    lst_class1.append(STU_LIST[index])
                json.dump(lst_class1, f, ensure_ascii=False, indent=4)
                lst_class1.clear()
        lst.pop(0)


def stu_pending():
    class Pending():
        def __init__(self):
            self.tasks = queue.Queue()
            with open ('pending_task.txt','r',encoding='utf-8') as f:
                for line in f:
                    self.tasks.put(line)

        def add_task(self,task):    #task 为字符串变量
            self.tasks.put(task)
            print('添加事项成功\n')

        def show_task(self):
            q = queue.Queue()
            while not self.tasks.empty():
                q.put(self.tasks.get())

            if q.empty():
                print("待办事项为空\n")
                return 0            #代表待办事项的个数

            else:
                print('待办事项如下：')
                i = 0               #表示有几条待办事项
                while not q.empty():
                    task = q.get()
                    self.tasks.put(task)
                    i += 1
                    print(f'{i}. {task}')
                print('\n')
                return i

        def remove_task(self,num):
            while num > self.tasks.qsize():
                print('输入无效,请重试！')
                num = eval(input('请输入要清除事项的序号：'))

            q = queue.Queue()
            while num:
                q.put(self.tasks.get())
                num -= 1

            for i in range(0,num-1):
                self.tasks.put(q.get())

        def save_task(self):
            q = queue.Queue()
            while not self.tasks.empty():
                q.put(self.tasks.get())
            with open('pending_task.txt','a+',encoding='utf-8') as f:
                while not q.empty():
                    task = q.get()
                    self.tasks.put(task)
                    f.write(str(task)+'\n')
                print('保存成功！\n')

    TODO = Pending()

    print("1.添加事项")
    print("2.删除事项")
    print('3.显示所有事项')
    print('4.保存待办事项')
    print("0.退出当前页面")

    flag = True
    while flag:
        a = eval(input("请输入整数指令:"))
        match a:
            case 1:
                b = input('请输入待办事项：')
                TODO.add_task(b)
            case 2:
                num = eval(input('请输入要清除事项的序号：'))
                TODO.remove_task(num)
            case 3:
                TODO.show_task()
            case 4:
                TODO.save_task()
            case 0:
                flag = False
            case _:
              print('输入无效，请重新输入！')


def main():
    """尽量不要修改此函数的代码, 此函数用于全局调用"""
    menu()
    user_choice = get_choice()
    while user_choice != 0:
        exec(user_choice)
        menu()
        user_choice = get_choice()


if __name__ == '__main__':
    stu_init()
    main()
