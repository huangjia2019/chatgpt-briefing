# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

# Set up OpenAI API credentials
openai.api_key = "替换成你的Key"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

# Extract the response from the API output
response_text = response.response['choices'][0]['message']['content']

# Print the response
print(response_text)