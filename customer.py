class Customer:
	customers = []
	def __init__(self , cust_name , cust_phoneNum):
		self.name = cust_name
		self.PhoneNum = cust_phoneNum

		

	
		Customer.customers.append([self.name , self.PhoneNum])


