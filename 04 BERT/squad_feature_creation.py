import pickle
from transformers.data.processors.squad import SquadV2Processor, squad_convert_examples_to_features
from transformers import BertTokenizer

# 初始化SQuAD Processor, 数据集, 和分词器
processor = SquadV2Processor()
train_examples = processor.get_train_examples('04 BERT/SQuAD')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# 将SQuAD 2.0示例转换为BERT输入特征
train_features = squad_convert_examples_to_features(
    examples=train_examples,
    tokenizer=tokenizer,
    max_seq_length=384,
    doc_stride=128,
    max_query_length=64,
    is_training=True,
    return_dataset=False,
    threads=1
)

# 将特征保存到磁盘上
with open('04 BERT/train_features.pkl', 'wb') as f:
    pickle.dump(train_features, f)