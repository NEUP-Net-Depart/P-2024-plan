# Task 3

请补充个人信息后，在此完成报告！

接入LLM的web-api
~~~python
import time
from zhipuai import ZhipuAI

questions = input('请输入你的问题：')

client = ZhipuAI(api_key="c5b203c6b5273632daba494387afdb75.MhywiWSvmqnf4DY4")  # 请填写您自己的APIKey

response = client.chat.asyncCompletions.create(
    model="glm-4-plus",  # 请填写您要调用的模型名称
    messages=[
        {
            "role": "user",
            "content":
                "questions"
}
],
)
task_id = response.id
task_status = ''
get_cnt = 0

while task_status != 'SUCCESS' and task_status != 'FAILED' and get_cnt <= 40:
    result_response = client.chat.asyncCompletions.retrieve_completion_result(id=task_id)
    print(result_response)
    task_status = result_response.task_status

    time.sleep(2)
    get_cnt += 1
~~~

@Author:  
@Email:
