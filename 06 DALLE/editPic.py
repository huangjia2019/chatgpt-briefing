import openai
import urllib.request

# Set the OpenAI API key
openai.api_key = "替换成你的Key"

# Generate image using the DALL-E API
prompt = "a baby inside the masked area of the image 'armnice_masked.jpg'"
response = openai.Image.create_edit(
  image=open("armnice_rgba.png", "rb"),
  mask=open("armnice_rgba_masked.png", "rb"),
  prompt=prompt,
  n=1,
  size="1024x1024"
)

# Download and display the generated image
image_url = response['data'][0]['url']

# 下载图片并保存到当前目录
urllib.request.urlretrieve(image_url, "baby_in_mask.png")

# 打印成功信息
print("图片已成功保存到当前目录！")