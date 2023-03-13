from transformers import BertTokenizer, BertForQuestionAnswering
import torch
import numpy as np

# Set the random seed for PyTorch and NumPy
torch.manual_seed(0)
np.random.seed(0)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForQuestionAnswering.from_pretrained('bert-base-uncased')

question, text = "What is the capital of China?", "The capital of China is Beijing."

inputs = tokenizer.encode_plus(question, text, add_special_tokens=True, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

answer_start_index = torch.argmax(outputs.start_logits)
answer_end_index = torch.argmax(outputs.end_logits) + 1

predict_answer_tokens = inputs['input_ids'][0][answer_start_index:answer_end_index]
predicted_answer = tokenizer.decode(predict_answer_tokens)

print("中国的首都是？", predicted_answer)  