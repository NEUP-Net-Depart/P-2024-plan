# Task 2

请补充个人信息后，在此完成报告！

@Author:  李心言 
@Email:  1129200163@qq.com 



README里面记一些学到的操作和语法吧





- 读写文件：

	```python
	#读取
	with open(file_name, 'r', encoding='utf-8') as file:
	            data = json.load(file)
	
	#写入
	with open(file_name, 'w', encoding='utf-8') as file:
	            json.dump([student.to_dict() for student in self.students], file, ensure_ascii=False, indent=4)
	#这里dump中的参数1是另写的遍历字典的函数
	```

- Student类：

	```python
	class Student:
	    #初始化
	    def __init__(self, stu_id: str, name: str):
	        self.stu_id = stu_id
	        self.name = name
		
	    #序列化到字典
	    def to_dict(self):
	        return {'学号': self.stu_id, '姓名': self.name}
	
	    #从字典反序列化
	    @classmethod
	    def from_dict(cls, data):
	        return cls(data['学号'], data['姓名'])
	
	    #提供信息
	    def __str__(self):
	        return f"学号: {self.stu_id}, 姓名: {self.name}"
	```

- logging日志

	```python 
	import logging
	
	#配置日志记录
	logging.basicConfig(filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
	
	#三种不同的日志记载类型
	logging.info()
	logging.error()
	logging.warning()
	```

- 队列

  ```python
  import queue
  
  #初始化队列
  newQueue=queue.Queue()
  
  #添加队列
  newQueue.put(1)
  newQueue.put("otto")
  newQueue.put(0.5)
  
  #删除队列
  newQueue.get()
  
  #展示队列
  for i, item in enumerate(list(newQueue),start=1):
      print(f"{i}.{item}")
  ```

  
