# -*- coding: utf-8 -*-
"""faiss_k-means_clustering_spam-mail.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V03_m26ZfHFiQPNsgvy1HyuXYOVCpTgp
"""

import time
import numpy as np
import faiss
import sys
import pandas as pd

# encode_text_spam.pyにてベクトル化したデータ csv
filename =sys.argv[1]  

# encode_text_spam.py でベクトル化する前の rawデータ 後で結合する
before_filename = sys.argv[2]  


# ベクトル化済みデータ読み取り
# bert-server にて 768次元のベクトル化された文章


df = pd.read_csv(filename,header=None)

dx = df.values.astype('float32') # dataframe→ndarray変換

#print(dx.shape)
#print(len(df))
#print(len(df.columns))

# prepare data

d = 768                         # ベクトルの次元(dimension)
nb = len(df)                    # データベースのサイズ(database size) = 今回は入力メールの件数

np.random.seed(1234)
x = np.random.random((nb, d)).astype('float32')

print(x.shape)
x[:, 0] += np.arange(nb) / 1000.

print(x.shape)
print(x)
x.dtype


'''
# GPUでの動かす場合のconfig

print("BUILD THE INDEX")
res = faiss.StandardGpuResources()
flat_config = faiss.GpuIndexFlatConfig()
index = faiss.GpuIndexFlatL2(res, d, flat_config)
print(index.is_trained)

'''


# クラスタリング　Kmeans分類

start = time.time() # 時間計測

# k クラスタ数
ncentroids =  sys.argv[3]

# イテレーション 試行回数
niter =  20 

verbose =  True

#d = x.shape [1]
d = dx.shape [1]

kmeans = faiss.Kmeans(d, ncentroids, niter = niter, verbose = verbose)

#kmeans.train(x)
kmeans.train(np.ascontiguousarray(dx))
#index_sim.add(np.ascontiguousarray(tr_features_np)) # np.ascontiguousarray こちら参考に https://github.com/facebookresearch/faiss/issues/459


train_elapsed_time = time.time() - start # 時間計測
print('train_elapsed_time:',train_elapsed_time)

# kの中心点はkmeans.centroids　で取り出す　形見てみる
#print(kmeans.centroids.shape)

# k=0　の中心の座標　
#print(kmeans.centroids[0])

#Assignment
#To compute the mapping from a set of vectors x to the cluster centroids after kmeans has finished training, use:

#割り当て
#kmeansがトレーニングを終了した後、ベクトルxのセットからクラスター重心へのマッピングを計算するには、次を使用します。

#D, I = kmeans.index.search(x, 1)

D, I = kmeans.index.search((np.ascontiguousarray(dx)), 1)


#This will return the nearest centroid for each line vector in x in I. D contains the squared L2 distances.
# 入力xベクトルに関して、最も近い(1)中心座標(nearest centroid)の　indexが　　　　Iに返される
# 入力xベクトルに関して、最も近い(1)中心座標(nearest centroid)の　2乗のL2距離が　Dに返される

print(I.shape)
#print(D.shape)

print(I[:,0])
#print(D)

df_text_k = pd.DataFrame(I[:,0], columns=['k_index'])
print(df_text_k.head)


df_before = pd.read_csv(before_filename)

df_result = df_before.join(df_text_k) #　クラスタ実施結果と元のcsvと結合
print(df_result.head)

df_result.to_csv('df_result.csv',index=False, header=True)
