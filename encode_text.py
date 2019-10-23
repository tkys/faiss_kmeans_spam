from bert_serving.client import BertClient
import numpy as np
import sys
import time

s_time = time.time()
text_list = [
    'こんにちは',
    'おはよう',
    'こんばんは',
    'お腹すいた',
    'ご飯食べたい',
    '明日晴れてると良いな',
    '明日の天気はどうだろうか',
    '雨降ったら嫌やな'
]

with BertClient(port=5555, port_out=5556) as bc:
    text_vecs = bc.encode(text_list)

e_time = time.time()-s_time

print(e_time)
np.savetxt('text_vecs.csv', text_vecs, delimiter=',')
