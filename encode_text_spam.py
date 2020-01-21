
from bert_serving.client import BertClient
import numpy as np
import sys
import time
import xlrd
import pandas as pd
import re


filename =sys.argv[1]
#df = pd.read_csv(filename, sep=',')  #csv
df = pd.read_excel(filename)  #excel
#print(df.info())

df = df.reset_index()  #'入力データがベクトル値しかないので、indexを振っておく
df = df[['index','本文']]  #カラム名'本文'
#print(df)


```文字列 削除 変換```
## DateFrame.replace(置換する文字列の正規表現パターン, 置換後の文字列, regex:正規表現を使う場合はTrue

#df = df.replace('https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", regex=True)
#df = df.replace('RT', "")
#df = df.replace('お気に入り', "")
#df = df.replace('まとめ', "")
#df = df.replace('[!-~]', "",regex=True) #半角記号,数字,英字
#df = df.replace('[︰-＠]', "",regex=True) #全角記号

df = df.replace( ' ',   '', regex=True) #スペース消しておく
df = df.replace( '\n', '-', regex=True) #改行置換　改行のみメールも対応 # bert-server　でテキスト無しは受け付けない為とりあえず-へ　 
df = df.replace( '',   '-', regex=True) #空メールむけ対応　#空のメール # bert-server　でテキスト無しは受け付けない為とりあえず-へ


#print('isnull =:',df.isnull())  # nullチェック

#df  = df.dropna()
df  = df.fillna('-') # Nan 対応 '-'へ

#index_list = df['index']


text_list = df['本文'].values.tolist()  # リスト化してbertに放り込む



s_time = time.time() #時間計測

with BertClient(port=5555, port_out=5556) as bc:
    text_vecs = bc.encode(text_list)

e_time = time.time()-s_time　
print('bert.encode time',e_time,'[sec]')

np.savetxt('text_vecs.csv', text_vecs, delimiter=',') # save # 768 dimention

#df_vecs = pd.DataFrame(text_vecs)
#print(df_vecs.shape)
#print(df_vecs.head)
#df_result = pd.concat([df['index'],df_vecs])  #concat 
#print(df_result.info())
#print(df_result.head)
