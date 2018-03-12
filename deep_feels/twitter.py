import tweepy
from tweepy import OAuthHandler

consumer_key = 'GqArA5wElrzL9bAMHMQNzaRKU'
consumer_secret = 'ohrsSg6v2HmbvAe5z3CH5wonAJ8ihjhyWJM0vrRToRqao43dwn'
access_token = '973038024136232961-e6R2HOQfMZ6prl2Z4fRfxz8MCVNERCP'
access_secret = 'nUs6Xzl4qWq9mM1H7mOthZDNSARJVc5ICvCiBCIs18n2V'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
  
api = tweepy.API(auth)


def tweets():
    statuses = [status.text for status in tweepy.Cursor(api.search, q = 'technology').items(10)]
    return statuses
