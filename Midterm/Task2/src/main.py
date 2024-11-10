# 学生管理系统

# PS: 可以仅以 “姓名” / “学号” 来代指学生信息

STU_LIST = []
STU_FILE = "TODO"


def stu_init():
    """此函数用于, 从文件中, 初始化学生信息"""
    pass


def get_choice() -> int:
    """此函数用于, 在命令行里, 获取用户输入的选项"""
    pass


def menu():
    """此函数用于, 在命令行里, 打印出菜单"""
    pass


def exec():
    """此函数用于, 根据用户输入的选项, 执行相应的功能"""
    pass


def stu_add():
    """此函数用于, 添加学生信息"""
    pass


def stu_del():
    """此函数用于, 删除学生信息"""
    pass


def stu_mod():
    """此函数用于, 修改学生信息"""
    pass


def stu_sel():
    """此函数用于, 查询学生信息"""
    pass


def stu_save():
    """此函数用于, 将学生信息保存到文件中"""
    pass


def exec():
    """此函数用于, 根据用户输入的选项, 执行相应的功能"""
    pass


def main():
    """尽量不要修改此函数的代码, 此函数用于全局调用"""
    user_choice = get_choice()
    while user_choice != 0:
        menu()
        exec(user_choice)
        user_choice = get_choice()
    pass


if __name__ == '__main__':
    main()
