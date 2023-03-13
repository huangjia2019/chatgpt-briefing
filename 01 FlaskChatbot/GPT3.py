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
    
    # Generate response from OpenAI GPT-3 API
    response = openai.Completion.create(
        engine="davinci",
        prompt=userText,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return str(response.choices[0].text.strip())

if __name__ == "__main__":
    app.run()
