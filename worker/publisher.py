import boto3
import json

client = boto3.client('sns')

sub = "keyword"
def sns_pub(msg,subject):
	msg = json.dumps(msg)
	response = client.publish(
	    TopicArn='arn:aws:sns:us-west-2:853781862143:MyTopic',
	    Message=msg,
	    Subject=sub,
	    MessageStructure='string',
	)

