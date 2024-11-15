# 学生管理系统

# PS: 可以仅以 “姓名” / “学号” 来代指学生信息

import json
import logging
import queue

STU_FILE = "../../resources/students.json"
LOG_FILE = "../../resources/students_log.txt"

# 配置日志记录
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Student:
    def __init__(self, stu_id: str, name: str):
        self.stu_id = stu_id
        self.name = name

    def to_dict(self):
        return {'学号': self.stu_id, '姓名': self.name}

    @classmethod
    def from_dict(cls, data):
        return cls(data['学号'], data['姓名'])

    def __str__(self):
        return f"学号: {self.stu_id}, 姓名: {self.name}"

class StudentManager:
    def __init__(self, file_name: str):
        self.students = []
        self.file_name = file_name
        self.stu_init()
        self.todo_queue = queue.Queue()

    def stu_init(self):
        """此函数用于, 从文件中, 初始化学生信息"""
        with open(self.file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.students = [Student.from_dict(student) for student in data]
            logging.info("学生信息加载成功")

    def stu_save(self):
        """此函数用于, 将学生信息保存到文件中"""
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump([student.to_dict() for student in self.students], file, ensure_ascii=False, indent=4)
            logging.info("学生信息保存成功")
            print("学生信息保存成功")

    def stu_add(self):
        """此函数用于, 添加学生信息"""
        stu_id = input("请输入学号: ")
        name = input("请输入姓名: ")
        self.students.append(Student(stu_id, name))
        print("学生信息添加成功!")
        logging.info(f"添加学生信息成功: 学号={stu_id}, 姓名={name}")

    def stu_del(self):
        """此函数用于, 删除学生信息"""
        stu_id = input("请输入要删除的学号: ")
        for student in self.students:
            if student.stu_id == stu_id:
                self.students.remove(student)
                print("学生信息删除成功!")
                logging.info(f"删除学生信息成功: 学号={stu_id}")
                return
        print("未找到该学号的学生信息!")
        logging.warning(f"未找到该学号的学生信息: 学号={stu_id}")

    def stu_mod(self):
        """此函数用于, 修改学生信息"""
        stu_id = input("请输入要修改的学号: ")
        for student in self.students:
            if student.stu_id == stu_id:
                new_name = input("请输入新的姓名: ")
                student.name = new_name
                print("学生信息修改成功!")
                logging.info(f"修改学生信息成功: 学号={stu_id}, 新姓名={new_name}")
                return
        print("未找到该学号的学生信息!")
        logging.warning(f"未找到该学号的学生信息: 学号={stu_id}")

    def stu_sel(self):
        """此函数用于, 查询学生信息"""
        stu_id = input("请输入要查询的学号: ")
        for student in self.students:
            if student.stu_id == stu_id:
                print(student)
                logging.info(f"查询学生信息成功: 学号={stu_id}")
                return
        print("未找到该学号的学生信息!")
        logging.warning(f"未找到该学号的学生信息: 学号={stu_id}")
        
    def stu_dis(self):
        """此函数用于，展示所有学生信息"""
        if not self.students:
            logging.info("当前没有学生信息")
            print("当前没有学生信息。")
        else:
            logging.info("展示所有学生信息")
            for student in self.students:
                print(student)
    
    def add_todo_item(self):
        """添加待办事项"""
        item = input("请输入待办事项: ")
        self.todo_queue.put(item)
        print("添加待办事项成功")
        logging.info(f"添加待办事项成功: {item}")

    def process_todo_item(self):
        """处理待办事项"""
        if not self.todo_queue.empty():
            item = self.todo_queue.get()
            print(f"处理待办事项: {item}")
            logging.info(f"处理待办事项成功: {item}")
        else:
            print("待办事项队列为空。")
            logging.info("待办事项队列为空")

    def display_todo_items(self):
        """展示所有待办事项"""
        if self.todo_queue.empty():
            print("待办事项队列为空。")
            logging.info("待办事项队列为空")
        else:
            print("待办事项列表:")
            for i, item in enumerate(list(self.todo_queue.queue), start=1):
                print(f"{i}. {item}")
            logging.info("展示所有待办事项")

manager = StudentManager(STU_FILE)



def get_choice() -> int:
    """此函数用于, 在命令行里, 获取用户输入的选项"""
    try:
        choice = int(input("请输入选项: "))
        return choice
    except ValueError:
        print("请输入有效的数字选项!")
        return get_choice()


def menu():
    """此函数用于, 在命令行里, 打印出菜单"""
    print("""
    学生管理系统
    1. 添加学生信息
    2. 删除学生信息
    3. 修改学生信息
    4. 查询学生信息
    5. 保存学生信息
    6. 展示所有学生信息
    7. 添加待办事项
    8. 处理待办事项
    9. 展示所有待办事项
    0. 退出
    """)


def exec(choice: int):
    """此函数用于, 根据用户输入的选项, 执行相应的功能"""
    if choice == 1:
        manager.stu_add()
    elif choice == 2:
        manager.stu_del()
    elif choice == 3:
        manager.stu_mod()
    elif choice == 4:
        manager.stu_sel()
    elif choice == 5:
        manager.stu_save()
    elif choice == 6:
        manager.stu_dis()
    elif choice == 7:
        manager.add_todo_item()
    elif choice == 8:
        manager.process_todo_item()
    elif choice == 9:
        manager.display_todo_items()
    elif choice == 0:
        print("退出系统")
    else:
        print("无效选项，请重新输入")



def main():
    """尽量不要修改此函数的代码, 此函数用于全局调用"""
    """最后还是修改了...稍微调整了一下代码顺序让操作更流畅"""
    user_choice = 1
    while user_choice != 0:
        menu()
        user_choice = get_choice()
        exec(user_choice)
    pass


if __name__ == '__main__':
    main()
