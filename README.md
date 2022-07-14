# NLP Skill Tree : 

## 1.Preprocessing(預/前處理) : 
- 以NLP來說，preprocessing通常包含兩個重要工作：爬蟲(crawling)及斷詞(tokenization)。
    - 1.crawling : 
        - 常用的爬蟲套件有requests和Beautiful Soup等等
    - 2.tokenization( = word segmentation) : 
        - Data cleaning
        - Word Cut, tokenization
        - stemming?!!
        - NLTK(Natural Language Tool Kit)
        - StopWords
        - vectorization (apply CountVectorizer) -> from sklearn.feature_extraction.text import CountVectorizer
        - !中文的tokenization特別會有粒度(granularity)的問題-> 相較英文，中文多了好幾種不同的斷詞方式。這是因為在中文裡，並沒有像英文裡空白的機制可以用來區分字與字之間的間隔。[Reference](https://medium.com/@derekliao_62575/nlp%E7%9A%84%E5%9F%BA%E6%9C%AC%E5%9F%B7%E8%A1%8C%E6%AD%A5%E9%A9%9F-i-%E8%AA%9E%E6%96%99%E7%9A%84%E9%A0%90%E8%99%95%E7%90%86-preprocessing-8538f0b763d6)

## 2.Modeling(建立語言模型) : 
    - 

## 3.Run and take the Result(執行任務/產出結果) : 
    - 