from transformers import BertForQuestionAnswering, BertTokenizer, BertForQuestionAnswering, AdamW
import torch
from torch.utils.data import TensorDataset

# 是否有GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 下载未经微调的BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForQuestionAnswering.from_pretrained('bert-base-uncased').to(device)

# 评估未经微调的BERT的性能
def china_capital():
    question, text = "What is the capital of China?", "The capital of China is Beijing."
    inputs = tokenizer.encode_plus(question, text, add_special_tokens=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs.to(device))
    answer_start_index = torch.argmax(outputs.start_logits)
    answer_end_index = torch.argmax(outputs.end_logits) + 1
    predict_answer_tokens = inputs['input_ids'][0][answer_start_index:answer_end_index]
    predicted_answer = tokenizer.decode(predict_answer_tokens)
    print("中国的首都是？", predicted_answer) 
china_capital()    

from transformers import BertTokenizer, BertForQuestionAnswering, AdamW
from torch.utils.data import DataLoader, RandomSampler, SequentialSampler
from transformers.data.processors.squad import SquadV2Processor, SquadExample, squad_convert_examples_to_features

# 加载SQuAD 2.0数据集的特征
import pickle
with open('04 BERT/SQuAD/train_features.pkl', 'rb') as f:
    train_features = pickle.load(f)

# 定义训练参数
train_batch_size = 8
num_epochs = 3
learning_rate = 3e-5

# 将特征转换为PyTorch张量
all_input_ids = torch.tensor([f.input_ids for f in train_features], dtype=torch.long)
all_attention_mask = torch.tensor([f.attention_mask for f in train_features], dtype=torch.long)
all_token_type_ids = torch.tensor([f.token_type_ids for f in train_features], dtype=torch.long)
all_start_positions = torch.tensor([f.start_position for f in train_features], dtype=torch.long)
all_end_positions = torch.tensor([f.end_position for f in train_features], dtype=torch.long)

train_dataset = TensorDataset(all_input_ids, all_attention_mask, all_token_type_ids, all_start_positions, all_end_positions)
num_samples = 100
train_dataset = TensorDataset(
    all_input_ids[:num_samples], 
    all_attention_mask[:num_samples], 
    all_token_type_ids[:num_samples], 
    all_start_positions[:num_samples], 
    all_end_positions[:num_samples])
train_sampler = RandomSampler(train_dataset)
train_dataloader = DataLoader(train_dataset, sampler=train_sampler, batch_size=train_batch_size)

# 加载BERT模型和优化器
model = BertForQuestionAnswering.from_pretrained('bert-base-uncased').to(device)
optimizer = AdamW(model.parameters(), lr=5e-5)

# 微调BERT
for epoch in range(num_epochs):
    for step, batch in enumerate(train_dataloader):
        model.train()
        optimizer.zero_grad()
        input_ids, attention_mask, token_type_ids, start_positions, end_positions = tuple(t.to(device) for t in batch)
        outputs = model(input_ids=input_ids, 
                        attention_mask=attention_mask, 
                        token_type_ids=token_type_ids, 
                        start_positions=start_positions, 
                        end_positions=end_positions)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

        # Print the training loss every 500 steps
        if step % 5 == 0:
            print(f"Epoch [{epoch+1}/{num_epochs}], Step [{step+1}/{len(train_dataloader)}], Loss: {loss.item():.4f}")

china_capital() 

# 保存微调后的模型
model.save_pretrained("04 BERT/SQuAD/SQuAD_finetuned_bert")