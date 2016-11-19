# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json
import re
# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '789309839977701376-BFk9HZRAtZ2pzmBUOh5h0TloHxda7Im'
ACCESS_SECRET = 'by8axgnWOv2vB1zHvyCEfKu3wi2Hu6sx8z71J6WgJQJUZ'
CONSUMER_KEY = 'uQ8DP9nfCQiBvTAvFMyjLSuUJ'
CONSUMER_SECRET = 'gODkNEkKu6HFzZgAG5tOpttJMNXyyG7CjIYCyG1TPt5dYSQH3k'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
keywords=["Google","Trump","Modi","Black Money"]
# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

def gettweet():
    iterator = twitter_stream.statuses.sample()
    iterator = twitter_stream.statuses.filter(track=','.join(keywords ), language="en")
    for tweet in iterator:
        j_text = json.loads(json.dumps(tweet))
        if not (j_text.has_key('coordinates') and j_text.has_key('place')):
            continue
        if j_text['coordinates'] is not None or j_text['place'] is not None:
            print tweet 
            keys =keyword_search(j_text['text'])
            if j_text['coordinates']:
                return j_text['text'], j_text['coordinates']
            return j_text['text'], j_text['place'],str(keys) 


def keyword_search(tweet_text):
    contains=[]
    for keyword in keywords:
        if re.search(keyword, tweet_text, re.IGNORECASE):
            contains.append(keyword)
    return contains
