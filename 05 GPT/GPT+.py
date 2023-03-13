import openai
openai.api_key = "替换成你的Key" 

# 调用 ChatGPT API 的函数
def ask_gpt(prompt, model, temperature=0.5):
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

# 示例使用 ChatGPT 进行对话
model = "text-davinci-003"
# model = "gpt-3.5-turbo"

# 初始化对话
conversation = ["Hello, how can I help you today?"]

while True:
    # 提示用户输入
    user_input = input("You: ")

    # 将用户输入添加到对话历史记录中
    conversation.append("User: " + user_input)

    # 将对话历史记录作为模型输入
    prompt = "\n".join(conversation)

    # 获取 ChatGPT 模型的回复
    response = ask_gpt(prompt, model)

    # 将回复添加到对话历史记录中
    conversation.append("AI: " + response)

    # 打印 ChatGPT 模型的回复
    print("AI: ", response)