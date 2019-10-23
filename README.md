# faiss_kmeans_spam

Large scale Spam-mails clustering k-means with Faiss for milion text-dataset

## Faiss
Fast large-scale KNN or k-means-clustering for Bilion target

## Bert-server
Use for text embedding (CPU/GPU)
dim =768

install
```
pip install bert-serving-server
pip install bert-serving-client
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
bert-serving-start -model_dir ./models/Japanese_L-12_H-768_A-12_E-30_BPE -num_worker=2
```

### ※
Every time bert-serv starts, new tmpABCDE files are created. 
For data disk capacity, when if you stop the process, delete the tmpABCDE files. 
