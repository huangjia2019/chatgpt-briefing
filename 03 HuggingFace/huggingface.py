# 导入必要的库
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from datasets import load_dataset

# 定义数据集名称和任务类型
dataset_name = "imdb"
task = "sentiment-analysis"

# 下载数据集并打乱数据
dataset = load_dataset(dataset_name)
dataset = dataset.shuffle()

# 初始化分词器和模型
model_name = "bert-base-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# 将文本编码为模型期望的张量格式
inputs = tokenizer(dataset["train"]["text"][:10], padding=True, truncation=True, return_tensors="pt")

# 将编码后的张量输入模型进行预测
outputs = model(**inputs)

# 获取预测结果和标签
predictions = outputs.logits.argmax(dim=-1)
labels = dataset["train"]["label"][:10]

# 打印预测结果和标签
for i, (prediction, label) in enumerate(zip(predictions, labels)):
    prediction_label = "正面评论" if prediction == 1 else "负面评论"
    true_label = "正面评论" if label == 1 else "负面评论"
    print(f"Example {i+1}: Prediction: {prediction_label}, True label: {true_label}")