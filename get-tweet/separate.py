import os
import json
import datetime


def separate_json(target):
    os.makedirs(target, exist_ok=True)

    # with open("/content/drive/MyDrive/rooma.json",'r',encoding="utf-8") as F:
    # with open("./rooma.json", 'r', encoding="utf-8") as F:
    with open(f"./{target}.json", 'r', encoding="utf-8") as F:
        # with open("./roomc.json", 'r', encoding="utf-8") as F:
        jsn = json.load(F)

    session_1_time = datetime.datetime(2020, 7, 4, 11, 10, 0)
    session_2_time = datetime.datetime(2020, 7, 4, 12, 20, 0)
    session_3_time = datetime.datetime(2020, 7, 4, 13, 30, 0)
    session_4_time = datetime.datetime(2020, 7, 4, 14, 40, 0)
    session_5_time = datetime.datetime(2020, 7, 4, 15, 50, 0)
    session_6_time = datetime.datetime(2020, 7, 4, 17, 00, 0)

    session_7_time = datetime.datetime(2020, 7, 5, 11, 10, 0)
    session_8_time = datetime.datetime(2020, 7, 5, 12, 20, 0)
    session_9_time = datetime.datetime(2020, 7, 5, 13, 30, 0)
    session_10_time = datetime.datetime(2020, 7, 5, 14, 40, 0)
    session_11_time = datetime.datetime(2020, 7, 5, 15, 50, 0)
    session_12_time = datetime.datetime(2020, 7, 5, 17, 00, 0)

    session_list_list = [[] for i in range(12)]

    for account in jsn:
        # dict = {'id': account['id'], 'date': account['date'],
        #         'time': account['time'], 'tweet': account['tweet']}
        # list.append(dict)
        # jsonから取れる
        date = account['date']
        time = account['time']
        # 日付＋時刻の文字列にフォーマットする
        date_time = f'{date} {time}'
        # ↑の文字列から、datetime型に変換
        tdatetime = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')

        if session_1_time < tdatetime and tdatetime < session_2_time:
            session_list_list[0].append(account)
        elif session_2_time < tdatetime and tdatetime < session_3_time:
            session_list_list[1].append(account)
        elif session_3_time < tdatetime and tdatetime < session_4_time:
            session_list_list[2].append(account)
        elif session_4_time < tdatetime and tdatetime < session_5_time:
            session_list_list[3].append(account)
        elif session_5_time < tdatetime and tdatetime < session_6_time:
            session_list_list[4].append(account)
        elif session_6_time < tdatetime and tdatetime < session_7_time:
            session_list_list[5].append(account)
        elif session_7_time < tdatetime and tdatetime < session_8_time:
            session_list_list[6].append(account)
        elif session_8_time < tdatetime and tdatetime < session_9_time:
            session_list_list[7].append(account)
        elif session_9_time < tdatetime and tdatetime < session_10_time:
            session_list_list[8].append(account)
        elif session_10_time < tdatetime and tdatetime < session_11_time:
            session_list_list[9].append(account)
        elif session_11_time < tdatetime and tdatetime < session_12_time:
            session_list_list[10].append(account)
        else:
            session_list_list[11].append(account)
    # print(list)

    for i, session_list in enumerate(session_list_list, 1):
        with open(f'{target}/session_{i}.json', mode='w', encoding='utf-8') as f:
            json.dump(session_list, f, ensure_ascii=False)

    # with open('session_2_list.json', mode='w', encoding='utf-8') as f:
    #     json.dump(session_list_list[1], f, ensure_ascii=False)

    # with open('session_3_list.json', mode='w', encoding='utf-8') as f:
    #     json.dump(session_list_list[2], f, ensure_ascii=False)

    # with open('session_4_list.json', mode='w', encoding='utf-8') as f:
    #     json.dump(session_list_list[3], f, ensure_ascii=False)

    # with open('session_5_list.json', mode='w', encoding='utf-8') as f:
    #     json.dump(session_list_list[4], f, ensure_ascii=False)

    # with open('session_6_list.json', mode='w', encoding='utf-8') as f:
    #     json.dump(session_list_list[5], f, ensure_ascii=False)

    # with open('session_7_list.json', mode='w', encoding='utf-8') as f:
    #     json.dump(session_list_list[6], f, ensure_ascii=False)

    # with open('session_8_list.json', mode='w', encoding='utf-8') as f:
    #     json.dump(session_list_list[7], f, ensure_ascii=False)

    # with open('session_9_list.json', mode='w', encoding='utf-8') as f:
    #     json.dump(session_list_list[8], f, ensure_ascii=False)

    # with open('session_10_list.json', mode='w', encoding='utf-8') as f:
    #     json.dump(session_list_list[9], f, ensure_ascii=False)

    # with open('session_11_list.json', mode='w', encoding='utf-8') as f:
    #     json.dump(session_list_list[10], f, ensure_ascii=False)

    # with open('session_12_list.json', mode='w', encoding='utf-8') as f:
    #     json.dump(session_list_list[11], f, ensure_ascii=False)


if __name__ == '__main__':
    separate_json('rooma')
    separate_json('roomb')
    separate_json('roomc')
