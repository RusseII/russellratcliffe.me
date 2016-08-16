from send_sms import sendText

class Engine_coin_flip():
	def __init__(self):
		print "creating engine object"

	def run(self):
		send=sendText()
		return send.send_text()


