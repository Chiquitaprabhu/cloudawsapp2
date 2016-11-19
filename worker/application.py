import flask
import sqs as mq
import sentiment 
import json
# import publisher

application = flask.Flask(__name__)


@application.route('/get_sentiment')
def index():
	sqsobj = mq.Sqs_Aws('queue1')
	tweet_jobg = sqsobj.getmsg()
	tweet_msg = json.loads(tweet_jobg.body)
	if tweet_msg:
		msg_s = sentiment.getdata(tweet_msg['msg'])
		if msg_s == '':
				return ''		
		msg_s = json.loads(msg_s)
		print type(msg_s)
		return str(tweet_msg)
	return ''		


if __name__ == '__main__':
	application.run()