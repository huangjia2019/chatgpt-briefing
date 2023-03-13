import openai
openai.api_key = "替换成你的Key" 

def ask_question(prompt, model, temperature=0.5):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=1024,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer = response.choices[0].text.strip()
    return answer

# 示例使用 GPT-3 进行问答
model = "text-davinci-002" 

# 示例问题
prompt = "What is the capital of China?"

# 获取答案
answer = ask_question(prompt, model)

print("Q: ", prompt)
print("A: ", answer)