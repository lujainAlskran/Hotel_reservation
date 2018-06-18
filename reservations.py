from Hotel import Hotel
from customer import Customer
from notification import Notification
class Reservations(Hotel , Customer , Notification):
	reservations = []
	def __init__(self):
		'''self.Hotelnum = hotel_number
		self.custNum = customer_number
		self.fromDate = from_date
		self.toDate = to_date'''
		pass


	# add reserve room
	def reserve_room(self , hotel_name,customer_name):
		hotel_num = 0
		for e in Hotel.hotels:
			if e[1] == hotel_name:
				if e[4] == 0:
					print "Sorry, There is no rooms in " + hotel_name + " try another hotel"
					return False
				else:
					hotel_num = e[0]
					e[4] -= 1
					return True
		
		print "There is no " + hotel_name	
		return False	
			
		
# add new reservation
	def add_new_reservation(self , hotel_name , customer_name, Cust_number , from_date , to_date):
		hotel_num = 0
		if Reservations.reserve_room(self , hotel_name , customer_name):
			for e in Hotel.hotels:
				if e[1] == hotel_name:
					hotel_num = e[0]
			Customer.customers.append([customer_name , Cust_number])
			cust_num = len(Customer.customers)
			Reservations.reservations.append([hotel_num,cust_num , from_date , to_date])
			Notification.send_text_message(self ,"Your reservation done , Thank you "+ customer_name , Cust_number)
			print "Done !"
	
	def list_resevrations_for_hotel(slef , hotel_name):
		cl = []
		for e in Hotel.hotels:
			if e[1] == hotel_name:
				Hotel_num = e[0]
		for i in Reservations.reservations:
			if i[0] == Hotel_num:
				if i[1]-1 < len(Customer.customers):
					cl.append(Customer.customers[i[1]-1])
		print "There is " + str(cl) + "in " + hotel_name