# Metrics class is used to obtain the current state of queue(total number of messages in the queue)
# and the total number of instances running.


class Metrics(object):

	def get_messages_in_queue(self):
		# get all the messages in the queue
		pass

	def get_number_workers(self):
		# get the numbers of currently running workers
		pass


if __name__ == '__main__':
	metrics=Metrics()
	print "Metrics object created"

