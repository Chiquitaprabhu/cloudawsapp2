import boto3


class Sqs_Aws():
   
	def __init__(self, QueueName):
		self.sqs = boto3.resource('sqs')
		try: 
			self.queue =self.sqs.get_queue_by_name(QueueName=QueueName)
		except:
			self.queue = self.sqs.create_queue(QueueName=QueueName)
		print self.queue.url

	def sendmsg(self, msg):
		# Create a new message
		response = self.queue.send_message(MessageBody=msg)

		# The response is NOT a resource, but gives you a message ID and MD5
		print response.get('MessageId')
		print response.get('MD5OfMessageBody')

	def getmsg(self):
		for message in self.queue.receive_messages():
			# message.delete()
			return message.body

	def deleteq(self):
		self.queue.delete()

		

