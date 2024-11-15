# Task 3

请补充个人信息后，在此完成报告！

@Author:  李心言 
@Email:  1129200163@qq.com 

参数调用依赖

```python
parser.add_argument('-g', '--global', choices=['local', 'web'])
```

来实现选择本地或是web上的ai模型



web的AI使用智谱glm-4-flash

本地AI使用Qwen/Qwen2.5-1.5B-Instruct

基本都是照着官方文档扒下来的代码，问题不是很大

实现了输入exit()退出ai的功能

本地ai因为文件大小的问题没有上传到仓库，本地运行的缺点是运行速度很慢..
