import logging
import openai
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

# 设置日志记录
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

# 设置 OpenAI API key
openai.api_key = "你的Open AI Key"

# 定义函数，处理 "/start" 命令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="我是一个机器人，请和我聊天吧！")

# 定义函数，使用 OpenAI 生成回复
async def generate_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 获取用户的消息
    message = update.message.text
    
    # 使用 OpenAI 生成回复
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message}\n",
        max_tokens=128,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    
    # 将回复发送给用户
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# 定义函数，处理未知命令
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="抱歉，我不明白您的命令。")
    
if __name__ == '__main__':
    # 设置 Telegram 机器人
    application = ApplicationBuilder().token('你的Telegram Token').build()
    
    # 添加 "/start" 命令处理器
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    # 添加消息处理器，使用 OpenAI 生成回复
    generate_response_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), generate_response)
    application.add_handler(generate_response_handler)    
    
    # 添加未知命令处理器
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

    # 启动机器人，并等待消息的到来
    application.run_polling()
