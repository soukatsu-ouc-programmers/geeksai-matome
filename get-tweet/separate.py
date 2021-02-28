import re
import json
import datetime

list = [] #リスト型を作る
with open("/content/drive/MyDrive/rooma.json",'r',encoding="utf-8") as F:
  jsn = json.load(F)

settion_1_time = datetime.datetime(2020, 7, 4, 11, 10, 0)
settion_2_time = datetime.datetime(2020, 7, 4, 12, 20, 0)
settion_3_time = datetime.datetime(2020, 7, 4, 13, 30, 0)
settion_4_time = datetime.datetime(2020, 7, 4, 14, 40, 0)
settion_5_time = datetime.datetime(2020, 7, 4, 15, 50, 0)
settion_6_time = datetime.datetime(2020, 7, 4, 17, 00, 0)

settion_7_time = datetime.datetime(2020, 7, 5, 11, 10, 0)
settion_8_time = datetime.datetime(2020, 7, 5, 12, 20, 0)
settion_9_time = datetime.datetime(2020, 7, 5, 13, 30, 0)
settion_10_time = datetime.datetime(2020, 7, 5, 14, 40, 0)
settion_11_time = datetime.datetime(2020, 7, 5, 15, 50, 0)
settion_12_time = datetime.datetime(2020, 7, 5, 17, 00, 0)

settion_list_list = [[]]*12

for account in jsn:
  dict = {'id': account['id'],'date': account['date'],'time':account['time'],'tweet':account['tweet']}
  list.append(dict)
  # jsonから取れる
  date = account['date']
  time = account['time']
  # 日付＋時刻の文字列にフォーマットする
  date_time = f'{date} {time}'
  # ↑の文字列から、datetime型に変換
  tdatetime = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
  # ターゲットとする日付時刻の定義

  if settion_1_time < tdatetime  and tdatetime < settion_2_time:
    settion_list_list[0].append(account)
  elif settion_2_time < tdatetime and tdatetime < settion_3_time:
    settion_list_list[1].append(account)
  elif settion_3_time < tdatetime and tdatetime < settion_4_time:
    settion_list_list[2].append(account)
  elif settion_4_time < tdatetime and tdatetime < settion_5_time:
    settion_list_list[3].append(account)
  elif settion_5_time < tdatetime and tdatetime < settion_6_time:
    settion_list_list[4].append(account)
  elif settion_6_time < tdatetime and tdatetime < settion_7_time:
    settion_list_list[5].append(account)
  elif settion_7_time < tdatetime and tdatetime < settion_8_time:
    settion_list_list[6].append(account)
  elif settion_8_time < tdatetime and tdatetime < settion_9_time:
    settion_list_list[7].append(account)
  elif settion_9_time < tdatetime and tdatetime < settion_10_time:
    settion_list_list[8].append(account)
  elif settion_10_time < tdatetime and tdatetime < settion_11_time:
    settion_list_list[9].append(account)
  elif settion_11_time < tdatetime and tdatetime < settion_12_time:
    settion_list_list[10].append(account)
  else:
    settion_list_list[11].append(account)
print(list)


with open('settion_1_list.json', 'w') as f:
  json.dump(settion_list_list[0], f , ensure_ascii=False)
from google.colab import files
files.download("settion_1_list.json")


with open('settion_2_list.json', 'w') as f:
  json.dump(settion_list_list[1], f , ensure_ascii=False)
from google.colab import files
files.download("settion_2_list.json")

with open('settion_3_list.json', 'w') as f:
  json.dump(settion_list_list[2], f , ensure_ascii=False)
from google.colab import files
files.download("settion_3_list.json")

with open('settion_4_list.json', 'w') as f:
  json.dump(settion_list_list[3], f , ensure_ascii=False)
from google.colab import files
files.download("settion_4_list.json")

with open('settion_5_list.json', 'w') as f:
  json.dump(settion_list_list[4], f , ensure_ascii=False)
from google.colab import files
files.download("settion_5_list.json")

with open('settion_6_list.json', 'w') as f:
  json.dump(settion_list_list[5], f , ensure_ascii=False)
from google.colab import files
files.download("settion_6_list.json")

with open('settion_7_list.json', 'w') as f:
  json.dump(settion_list_list[6], f , ensure_ascii=False)
from google.colab import files
files.download("settion_7_list.json")

with open('settion_8_list.json', 'w') as f:
  json.dump(settion_list_list[7], f , ensure_ascii=False)
from google.colab import files
files.download("settion_8_list.json")

with open('settion_9_list.json', 'w') as f:
  json.dump(settion_list_list[8], f , ensure_ascii=False)
from google.colab import files
files.download("settion_9_list.json")

with open('settion_10_list.json', 'w') as f:
  json.dump(settion_list_list[9], f , ensure_ascii=False)
from google.colab import files
files.download("settion_10_list.json")

with open('settion_11_list.json', 'w') as f:
  json.dump(settion_list_list[10], f , ensure_ascii=False)
from google.colab import files
files.download("settion_11_list.json")

with open('settion_12_list.json', 'w') as f:
  json.dump(settion_list_list[11], f , ensure_ascii=False)
from google.colab import files
files.download("settion_12_list.json")

