"""
API使うやつ
"""
# import config
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

from apscheduler.schedulers.blocking import BlockingScheduler

# 収集対象のルーム
# room = 'geettest'


def get_tweet(name, hashTag):
    # DB関連の準備
    DATABASE_URL = os.getenv('DATABASE_URL')
    engine = create_engine(DATABASE_URL)

    Base = declarative_base()

    # スキーム定義
    class Tweet(Base):
        __tablename__ = name
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

    def search(params):
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

    statuses = []

    now = datetime.now()
    since = (now - timedelta(hours=1, minutes=10)
             ).strftime('%Y-%m-%d_%H:%M:%S_JST')
    until = now.strftime('%Y-%m-%d_%H:%M:%S_JST')

    params = {
        'q': f'#技育祭 #{hashTag} since:{since} until:{until} exclude:retweets', 'count': 100}
    tweets = search(params)
    statuses.extend(tweets['statuses'])
    sleep(10)
    while 'next_results' in tweets['search_metadata'].keys():
        next_results = tweets['search_metadata']['next_results'].lstrip('?')
        params = parseToParam(next_results)
        # params['q'] = params['q'].replace('%25', '%')
        params['q'] = urllib.parse.unquote(params['q'])
        print(params)
        tweets = search(params)
        statuses.extend(tweets['statuses'])
        sleep(10)

    store_data = [
        Tweet(tweet_str_id=v['id_str'],
              # 'tweet_time': datetime.strptime(v['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(timezone(timedelta(hours=+9))).strftime('%Y-%m-%d %H:%M:%S')
              created_at=datetime.strptime(v['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(
            timezone(timedelta(hours=+9)))
        ) for v in statuses]
    print(len(store_data))
    # DBに保存
    session.bulk_save_objects(
        store_data, return_defaults=True
    )

    session.commit()
    print(f'saved {name}')

    # # jsonに保存
    # store_data = [
    #     {'tweet_id': v['id_str'],
    #     # 'tweet_time': datetime.strptime(v['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(timezone(timedelta(hours=+9))).strftime('%Y-%m-%d %H:%M:%S')
    #     'tweet_time': datetime.strptime(v['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(timezone(timedelta(hours=+9)))
    #     } for v in statuses]
    
    # with open('api-out.json', mode='w', encoding='utf-8') as f:
    #     # json.dump(tmp_list, f, ensure_ascii=False)
    #     json.dump(store_data, f, ensure_ascii=False)
    # # print(tweets)


sched = BlockingScheduler()
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 14, 40, 0), args=['holeA_Day1_1', 'ホールA'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 14, 40, 0), args=['holeB_Day1_1', 'ホールB'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 14, 40, 0), args=['holeC_Day1_1', 'ホールC'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 14, 40, 0), args=['room1_Day1_1', 'room1'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 14, 40, 0), args=['room2_Day1_1', 'room2'])

sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 15, 50, 0), args=['holeA_Day1_2', 'ホールA'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 15, 50, 0), args=['holeB_Day1_2', 'ホールB'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 15, 50, 0), args=['holeC_Day1_2', 'ホールC'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 15, 50, 0), args=['room1_Day1_2', 'room1'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 15, 50, 0), args=['room2_Day1_2', 'room2'])

sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 17, 0, 0), args=['holeA_Day1_3', 'ホールA'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 17, 0, 0), args=['holeB_Day1_3', 'ホールB'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 17, 0, 0), args=['holeC_Day1_3', 'ホールC'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 17, 0, 0), args=['room1_Day1_3', 'room1'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 17, 0, 0), args=['room2_Day1_3', 'room2'])

sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 18, 10, 0), args=['holeA_Day1_4', 'ホールA'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 18, 10, 0), args=['holeB_Day1_4', 'ホールB'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 18, 10, 0), args=['holeC_Day1_4', 'ホールC'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 18, 10, 0), args=['room1_Day1_4', 'room1'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 18, 10, 0), args=['room2_Day1_4', 'room2'])


sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 14, 40, 0), args=['holeA_Day2_1', 'ホールA'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 14, 40, 0), args=['holeB_Day2_1', 'ホールB'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 14, 40, 0), args=['holeC_Day2_1', 'ホールC'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 14, 40, 0), args=['room1_Day2_1', 'room1'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 14, 40, 0), args=['room2_Day2_1', 'room2'])

sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 15, 50, 0), args=['holeA_Day2_2', 'ホールA'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 15, 50, 0), args=['holeB_Day2_2', 'ホールB'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 15, 50, 0), args=['holeC_Day2_2', 'ホールC'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 15, 50, 0), args=['room1_Day2_2', 'room1'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 15, 50, 0), args=['room2_Day2_2', 'room2'])

sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 17, 0, 0), args=['holeA_Day2_3', 'ホールA'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 17, 0, 0), args=['holeB_Day2_3', 'ホールB'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 17, 0, 0), args=['holeC_Day2_3', 'ホールC'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 17, 0, 0), args=['room1_Day2_3', 'room1'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 17, 0, 0), args=['room2_Day2_3', 'room2'])

sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 18, 10, 0), args=['holeA_Day2_4', 'ホールA'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 18, 10, 0), args=['holeB_Day2_4', 'ホールB'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 18, 10, 0), args=['holeC_Day2_4', 'ホールC'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 18, 10, 0), args=['room1_Day2_4', 'room1'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 12, 18, 10, 0), args=['room2_Day2_4', 'room2'])


sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 12, 10, 0), args=['holeA_Day3_1', 'ホールA'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 12, 10, 0), args=['holeB_Day3_1', 'ホールB'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 12, 10, 0), args=['holeC_Day3_1', 'ホールC'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 12, 10, 0), args=['room1_Day3_1', 'room1'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 12, 10, 0), args=['room2_Day3_1', 'room2'])

sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 14, 40, 0), args=['holeA_Day3_2', 'ホールA'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 14, 40, 0), args=['holeB_Day3_2', 'ホールB'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 14, 40, 0), args=['holeC_Day3_2', 'ホールC'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 14, 40, 0), args=['room1_Day3_2', 'room1'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 14, 40, 0), args=['room2_Day3_2', 'room2'])

sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 15, 50, 0), args=['holeA_Day3_3', 'ホールA'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 15, 50, 0), args=['holeB_Day3_3', 'ホールB'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 15, 50, 0), args=['holeC_Day3_3', 'ホールC'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 15, 50, 0), args=['room1_Day3_3', 'room1'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 15, 50, 0), args=['room2_Day3_3', 'room2'])

sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 17, 0, 0), args=['holeA_Day3_4', 'ホールA'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 17, 0, 0), args=['holeB_Day3_4', 'ホールB'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 17, 0, 0), args=['holeC_Day3_4', 'ホールC'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 17, 0, 0), args=['room1_Day3_4', 'room1'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 17, 0, 0), args=['room2_Day3_4', 'room2'])

sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 18, 10, 0), args=['holeA_Day3_5', 'ホールA'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 18, 10, 0), args=['holeB_Day3_5', 'ホールB'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 18, 10, 0), args=['holeC_Day3_5', 'ホールC'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 18, 10, 0), args=['room1_Day3_5', 'room1'])
sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 13, 18, 10, 0), args=['room2_Day3_5', 'room2'])

# sched.add_job(get_tweet, 'date', run_date=datetime(2021, 3, 11, 5, 59, 0), args=['test', 'room2'])

sched.start()