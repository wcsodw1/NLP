# python test.py

# from transformers import BertTokenizer, BertModel
# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# model = BertModel.from_pretrained("bert-base-uncased")
# text = "Hello, my dog is cute"
# encoded_input = tokenizer(text, max_length=100,
#                           add_special_tokens=True, truncation=True,
#                           padding=True, return_tensors="pt")
# output = model(**encoded_input)
# last_hidden_state, pooler_output = output[0], output[1]
# print("last_hidden_state", last_hidden_state.shape)
# print("pooler_output", pooler_output.shape)


# 1. BertConfig
# transformers.BertConfig 可以自定義 Bert 模型的架構，參數都是可選的
from transformers import BertTokenizer
# import argparse
# from transformers import BertModel, BertConfig
# configuration = BertConfig()  # 进行模型的配置，变量为空即使用默认参数
# model = BertModel(configuration)  # 使用自定义配置实例化 Bert 模型
# configuration = model.config  # 查看模型参数

# 2. BertTokenizer

tokenizer = BertTokenizer(vocab_file='bert-base-uncased-vocab.txt')
