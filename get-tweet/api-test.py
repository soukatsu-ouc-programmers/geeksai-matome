"""
API使うやつ
"""
import config
from requests_oauthlib import OAuth1Session
import json
from datetime import *
from time import sleep
import urllib

import os
import psycopg2
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 収集対象のルーム
room = 'tracka'

# DB関連の準備
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)

Base = declarative_base()

# スキーム定義
class Tweet(Base):
    __tablename__ = room
    id = Column(Integer, primary_key=True)
    tweet_str_id = Column(TEXT)
    created_at = Column(TIMESTAMP)

SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# テーブル作成
Base.metadata.create_all(engine)

# Twitterからデータ取得
# api_key = os.getenv('TW_API_KEY')
# api_secret_key = os.getenv('TW_API_SECRET_KEY')
# access_token = os.getenv('TW_ACCESS_TOKEN')
# access_token_secret = os.getenv('TW_ACCESS_TOKEN_SECRET')
api_key = config.TW_API_KEY
api_secret_key = config.TW_API_SECRET_KEY
access_token = config.TW_ACCESS_TOKEN
access_token_secret = config.TW_ACCESS_TOKEN_SECRET


def search(params):
    # params = { 'q': '#DeNATechCon since:2021-03-03_06:00:00_JST until:2021-03-03_08:00:00_JST exclude:retweets', 'count': 100 }
    # params = { 'q': '#DeNATechCon since:2021-03-03_13:00:00_JST until:2021-03-03_14:00:00_JST exclude:retweets', 'count': 100 }
    twitter = OAuth1Session(api_key, api_secret_key,
                            access_token, access_token_secret)
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    res = twitter.get(url, params=params)
    tweets = json.loads(res.text)
    return tweets


def parseToParam(parse_str, parse=None):
    if parse is None:
        parse = '&'
    return_params = {}
    parsed_str = parse_str.split(parse)
    for param_string in parsed_str:
        param, value = param_string.split('=', 1)
        return_params[param] = value
    return return_params


# store_data = [
#         Tweet(tweet_str_id=v['id_str'],
#         # 'tweet_time': datetime.strptime(v['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(timezone(timedelta(hours=+9))).strftime('%Y-%m-%d %H:%M:%S')
#         created_at=datetime.strptime(v['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(timezone(timedelta(hours=+9)))
#          ) for v in tweets['statuses']]
# tmp_list = []
statuses = []
# tweets = json.loads(res.text)
params = {'q': '#DeNATechCon since:2021-03-03_13:00:00_JST until:2021-03-03_14:00:00_JST exclude:retweets', 'count': 100}
tweets = search(params)
statuses.extend(tweets['statuses'])
sleep(10)
# if 'next_results' in tweets['search_metadata'].keys():
while 'next_results' in tweets['search_metadata'].keys():
    next_results = tweets['search_metadata']['next_results'].lstrip('?')
    params = parseToParam(next_results)
    # params['q'] = params['q'].replace('%25', '%')
    params['q'] = urllib.parse.unquote(params['q'])
    print(params)
    tweets = search(params)
    statuses.extend(tweets['statuses'])
    sleep(10)

# store_data = [
#     {'tweet_id': v['id_str'],
#     # 'tweet_time': datetime.strptime(v['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(timezone(timedelta(hours=+9))).strftime('%Y-%m-%d %H:%M:%S')
#     'tweet_time': datetime.strptime(v['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(timezone(timedelta(hours=+9)))
#     } for v in statuses]
store_data = [
        Tweet(tweet_str_id=v['id_str'],
        # 'tweet_time': datetime.strptime(v['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(timezone(timedelta(hours=+9))).strftime('%Y-%m-%d %H:%M:%S')
        created_at=datetime.strptime(v['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(timezone(timedelta(hours=+9)))
         ) for v in statuses]
print(len(store_data))
# DBに保存
# session.bulk_save_objects(
#     [Test(name=d) for d in data_list], return_defaults=True
# )
session.bulk_save_objects(
    store_data, return_defaults=True
)

session.commit()

# # jsonに保存
# with open('api-out.json', mode='w', encoding='utf-8') as f:
#     # json.dump(tmp_list, f, ensure_ascii=False)
#     json.dump(store_data, f, ensure_ascii=False)
# # print(tweets)
