"""
API使うやつ
"""
# import config
from requests_oauthlib import OAuth1Session
import json
from datetime import *

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
api_key = os.getenv('TW_API_KEY')
api_secret_key = os.getenv('TW_API_SECRET_KEY')
access_token = os.getenv('TW_ACCESS_TOKEN')
access_token_secret = os.getenv('TW_ACCESS_TOKEN_SECRET')
# api_key = config.TW_API_KEY
# api_secret_key = config.TW_API_SECRET_KEY
# access_token = config.TW_ACCESS_TOKEN
# access_token_secret = config.TW_ACCESS_TOKEN_SECRET

twitter = OAuth1Session(api_key, api_secret_key, access_token, access_token_secret)

url = 'https://api.twitter.com/1.1/search/tweets.json'
# params = {'q' : '#DeNATechCon since:2021-03-03_06:00:00_JST until:2021-03-03_08:00:00_JST exclude:retweets', 'count': 100}
params = { 'q': '#DeNATechCon since:2021-03-03_13:00:00_JST until:2021-03-03_14:00:00_JST exclude:retweets', 'count': 100 }

res = twitter.get(url, params = params)

tweets = json.loads(res.text)

store_data = [
        Tweet(tweet_str_id=v['id_str'],
        # 'tweet_time': datetime.strptime(v['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(timezone(timedelta(hours=+9))).strftime('%Y-%m-%d %H:%M:%S')
        created_at=datetime.strptime(v['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(timezone(timedelta(hours=+9)))
         ) for v in tweets['statuses']]

# session.bulk_save_objects(
#     [Test(name=d) for d in data_list], return_defaults=True
# )
session.bulk_save_objects(
    store_data, return_defaults=True
)

session.commit()

# jsonに保存
# with open('api-out.json', mode='w', encoding='utf-8') as f:
#     tweets = json.loads(res.text)
#     store_data = [
#         {'tweet_id': v['id_str'],
#         # 'tweet_time': datetime.strptime(v['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(timezone(timedelta(hours=+9))).strftime('%Y-%m-%d %H:%M:%S')
#         'tweet_time': datetime.strptime(v['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(timezone(timedelta(hours=+9)))
#         } for v in tweets['statuses']]
#     # json.dump(tweets, f, ensure_ascii=False)
#     json.dump(store_data, f, ensure_ascii=False)
# print(tweets)
