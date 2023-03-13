import openai
import urllib.request

# 设置 OpenAI API 密钥
openai.api_key = "替换成你的Key"

# 使用 DALL-E API 生成一张图片
response = openai.Image.create(
    prompt="一只骑着猫的老鼠,在宇宙中，非常梦幻",
    n=1,
    size="1024x1024"
)
image_url = response["data"][0]["url"]

# 下载图片并保存到当前目录
urllib.request.urlretrieve(image_url, "mouse_riding_cat_univ.png")

# 打印成功信息
print("图片已成功保存到当前目录！")
