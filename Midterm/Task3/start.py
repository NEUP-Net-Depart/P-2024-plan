import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer
from zhipuai import ZhipuAI
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

client = ZhipuAI(api_key="b9c831c06f60d6839d38d1f6c2acc342.y6cFjJwI5lj1IZav")
 

parser = argparse.ArgumentParser(description='AI')

parser.add_argument('-g', '--global_os', choices=['local', 'web'])

args = parser.parse_args()


model_name = "Qwen/Qwen2.5-1.5B-Instruct"

if args.global_os == 'local':
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype="auto",
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    prompt = input("user:")
    if prompt == "exit()":
        exit()
    messages = [
        {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=512
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    print(response)

elif args.global_os == 'web':
    while True:
        prompt = input("user:")
        if prompt == "exit()":
            exit()
        response = client.chat.completions.create(
            model="glm-4-flash",  
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        answer = response.choices[0].message.content
        print("ZhipuAI:",answer)