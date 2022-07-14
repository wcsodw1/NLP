# python NLP_TF_Keras_RealData.py
# cd C:/Users/user/Desktop/Github_NEW/AI/NLP/Text_Classfication/Sentiment_Analysis/Tensorflow_Keras
'''
Describe : 將文字轉成向量, 才能進行後續運算
'''
import os
import tensorflow as tf
from numpy import array
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 測試資料
docs = ['Well done!',
        'Good work',
        'Great effort',
        'nice work',
        'Excellent!',
        'Weak',
        'Poor effort!',
        'not good',
        'poor work',
        'Could have done better.']

vocab_size = 50
maxlen = 4

# 先轉成 one-hot encoding
encoded_docs = [one_hot(d, vocab_size) for d in docs]
print("encoded_docs :", encoded_docs)
print("encoded_docs.length :", len(encoded_docs))

# 轉成固定長度，長度不足則後面補空白
padded_docs = pad_sequences(encoded_docs, maxlen=maxlen, padding='post')

# 模型只有 Embedding
model = tf.keras.Sequential()
model.add(layers.Embedding(vocab_size, 64, input_length=maxlen))
model.compile('rmsprop', 'mse')

# 預測
output_array = model.predict(padded_docs)
print(output_array)
print(output_array.shape)
