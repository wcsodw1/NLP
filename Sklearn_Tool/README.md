
# 

from sklearn.utils import shuffle

from sklearn.pipeline import Pipeline

from sklearn.naive_bayes import MultinomialNB

from sklearn.linear_model import SGDClassifier

from sklearn.datasets import fetch_20newsgroups

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.naive_bayes import GaussianNB # 貝氏分類器

# TSNE : 降維工具 : 
- from sklearn.manifold import TSNE


# k-means 設置分群數量 : 
- from sklearn import cluster
- ex : kmeans = cluster.KMeans(n_clusters=NUM_CLUSTERS)

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA


from sklearn import metrics

#
本文覆盖的NLP方法有:

TF-IDF
Count Features
Logistic Regression
Naive Bayes
SVM
Xgboost
Grid Search
Word Vectors
Dense Network
LSTM
GRU
Ensembling
