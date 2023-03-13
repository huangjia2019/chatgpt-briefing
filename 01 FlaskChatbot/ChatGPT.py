from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set up OpenAI API authentication
openai.api_key = "替换成你的Key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    messages = []
    messages.append({"role":"user","content": userText})
    # Generate response from OpenAI GPT-3 API
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return str(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    app.run()


