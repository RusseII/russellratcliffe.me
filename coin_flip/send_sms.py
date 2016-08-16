# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
from random import *

# Find these values at https://twilio.com/user/account
account_sid = "AC6d430b1fae20daa6dfa9907ac1576456"
auth_token = "30b9b6d5a5b61d37024bb82f16fa4310"
client = TwilioRestClient(account_sid, auth_token)

class sendText():
	def __init__(self):
		print "created a sendText object"

	def send_text(self):

		numbers=['+13304146700','+17404579793']

		num=random()

		if num>=.5:
		    result="The flip is heads. Russell has to drive :*"
		else:
		    result="the flip is tails. Grace has to drive :*"
		print result
		for items in numbers:
		     message = client.messages.create(to=items, from_="+13304224104", body =result)
