class Hotel:
	hotels = []
	def __init__(self ,hotel_number ,hotel_name , city , total_room , empty_room ):
		self.num = hotel_number
		self.name = hotel_name
		self.city = city
		self.TotalRoom = total_room
		self.EmptyRoom = empty_room

		'''if self.name in Hotel.hotels:
			print "This hotel is in the list"
		else:'''
		Hotel.hotels.append([self.num,self.name,self.city,self.TotalRoom,self.EmptyRoom])

	def list_hotels_in_city(self , city):
		hotels_list = []
		for e in Hotel.hotels:
			if e[2] == city:
				hotels_list.append([e[1],str(e[3])+" room"])
		if hotels_list == []:
			print "There is no hotels in " + city
		else:
			print "In "+ city + " there is " + str(hotels_list)