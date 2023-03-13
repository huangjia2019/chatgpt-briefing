import openai

openai.api_key="替换成你的Key"
messages = []
system_message = input("您好，我们终于见面了！！您希望接下来我为您提供什么服务？")
messages.append({"role":"system","content":system_message})
print("\n")

print("好的，明白了! 我会服务好您的。" + "\n" + "现在请和我聊天吧！")

print("\n")
message = input("人类说：")
messages.append({"role":"user","content": message})

response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages
)

reply = response["choices"][0]["message"]["content"]
print("ChatGPT说: ", reply)