import argparse
import requests
import accelerate
from zhipuai import ZhipuAI
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

def local_llm(order):
    try:
        dir = r"D:\localllm\Qwen2.5-1.5B"
        tokenizer = AutoTokenizer.from_pretrained(dir)
        model = AutoModelForCausalLM.from_pretrained(
            dir,
            torch_dtype="auto",
            device_map="auto"
        )
        pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

        response = pipe(order, max_new_tokens=512)
        print("robot:", response[0]['generated_text'])
    except Exception as e:
        print("模型调用出错:", e)
    
    
def web_llm(order):
    client = ZhipuAI(api_key="512f1441f4eaf20816827cf2adc7ba25.wpCWSWFeurFNjCnU")
    response = client.chat.completions.create(
    model="glm-4-plus",  
    messages=[
        {"role": "user", "content": order},
        ],
    )
    print("robot:", response.choices[0].message.content)
    
    
def llm():
    parser = argparse.ArgumentParser(description='简单命令行聊天机器人')
    parser.add_argument('-g', '--globa', choices=['web', 'local'], required=True,
                        help='选择使用web-api还是本地模型')
    args = parser.parse_args()
    
    print(f"welcome to {args.globa} big model,enter \'quit\' to quit.")
    
    while True:
        order = input("you:")
        if order == "quit":
            break
        
        if args.globa == 'web':
            web_llm(order)
        if args.globa == 'local':
            local_llm(order)
            

if __name__ == "__main__":
    llm()