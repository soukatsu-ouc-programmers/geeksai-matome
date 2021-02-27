import config
from requests_oauthlib import OAuth1Session
import json


api_key = config.API_KEY
api_secret_key = config.API_SECRET_KEY
access_token = config.ACCESS_TOKEN
access_token_secret = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(api_key, api_secret_key, access_token, access_token_secret)

url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q' : '%23坂道テレビ%20%23櫻坂46%20exclude:retweets', 'count': 100}

res = twitter.get(url, params = params)

with open('api-out.json', mode='w', encoding='utf-8') as f:
    tweets = json.loads(res.text)
    json.dump(tweets, f, ensure_ascii=False)
# print(tweets)
