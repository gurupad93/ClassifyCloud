class Worker:
	
	def run(self):
		"""
		Get the request queue
		Get the response queue
		Get the terminate queue
		In loop keep checking for the messages in terminate queue
		If the differnece between message timestamp and current time is more than 4 seconds, it is considered as a expiered request.
		Note: For now, we are planning to keep the TTL to 4 seconds.
		else it is considered as a valid request.
		"""
		print "Worker ran"
		pass 

def main():
	#create a worker object
	worker=Worker()
	
	#call the run method of worker in loop
	worker.run()

if __name__ == '__main__':
	main()
    
