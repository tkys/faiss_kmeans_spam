# faiss_kmeans_spam

High-speed clustering of large-scale data (spam-mail text) using Bert-server and Faiss.

Bert-server と Faiss を利用した大規模データ（spam-mail text）の高速クラスタリング.

----

## Faiss

A library for efficient similarity search and clustering of dense vectors.

Super fast k-means / KNN can be used with python on CPU / GPU machines.


install
```
pip faiss-cpu
or
pip faiss-gpu

```

## Bert-server

Use for text embedding (CPU/GPU)

dim =768


install
```
pip install bert-serving-server
pip install bert-serving-client

pip install tensorflow-cpu 　
or 
pip install tensorflow-gpu 　

```

## Get pre-trainded model　(Japanese) 

and unzip under the '/models' directory


LINK:
http://nlp.ist.i.kyoto-u.ac.jp/DLcounter/lime.cgi?down=http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/JapaneseBertPretrainedModel/Japanese_L-12_H-768_A-12_E-30_BPE.zip&name=Japanese_L-12_H-768_A-12_E-30_BPE.zip

```
mkdir ./models
cd ./models
wget http://nlp.ist.i.kyoto-u.ac.jp/DLcounter/lime.cgi?down=http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/JapaneseBertPretrainedModel/Japanese_L-12_H-768_A-12_E-30_BPE.zip&name=Japanese_L-12_H-768_A-12_E-30_BPE.zip
unzip ./Japanese_L-12_H-768_A-12_E-30_BPE.zip

ls -al ./Japanese_L-12_H-768_A-12_E-30_BPE/

bert_config.json
bert_model.ckpt.data-00000-of-00001
bert_model.ckpt.index
bert_model.ckpt.meta
pytorch_model.bin
README.txt
vocab.txt

```

## Start bert-server

```
bert-serving-start -model_dir ./models/Japanese_L-12_H-768_A-12_E-30_BPE -num_worker=2  -max_seq_len=300
```

### ※
Every time bert-serv starts, new tmpABCDE files are created. 

<b>For data disk capacity, when if you stop the process, delete the tmpABCDE files.</b> 

----


## Input text

input_text.csv

columns = '本文'
```
本文
日頃よりご利用ありがとうございます。\n至急お伝えせねばならない事があります為、下記よりご確認ください。\nhttp://abcsefg.com
現在ご利用されている端末以外で、@docomo.ne.jpでご利用中アカウントへのログインされました。\n身に覚えがない場合には下記より停止をご確認ください。\n↓詳細確認↓\nabcsefg.com\n▼ログイン必要情報▼
:
:


````
## Get word-vector
```
python encode_text_spam.py  ./path/to/input_text.csv  # or .xlsx

>>> text_vecs.csv is generated
```


## Clustering Faiss
```
python faiss_clustering_spam_mail.py　{/path/to/text_vecs.csv} {./path/to/input_text.csv} {cluster_number}

example.
python faiss_clustering_spam_mail.py　text_vecs.csv input_text.csv 100  # cluster_number K=100

>>> df_result.csv  is generated
```


