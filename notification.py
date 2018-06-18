from twilio.rest import Client
class Notification:
	# Send message for customer
	def send_text_message(self ,message, number):
		account_sid = "ACde86f6f31ac92acadc62ca667fabe720"
	# Your Auth Token from twilio.com/console
		auth_token  = "b92e6e71120f84bbdcc2fb80f349e4ba" #who i am

		client = Client( account_sid, auth_token)	

		message = client.messages.create(
    		to=number,
    		from_="+19592084162",
    		body=message)