import sqs as mq
import twitter_streaming as tstream
import json
# import sentiment as stext
# import time 

sqsobj = mq.Sqs_Aws('queue1')
tweet_msg, tweet_coordinate, tweet_keywords = tstream.gettweet()
t_jobg =  {'msg':tweet_msg,'loc':tweet_coordinate,'keywords':tweet_keywords}
t_jobg = json.dumps(t_jobg)
# stext.getdata(tweet_msg)
sqsobj.sendmsg(t_jobg)
# time.sleep(5)
# sqsobj.getmsg()

