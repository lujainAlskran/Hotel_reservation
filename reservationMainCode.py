from twilio.rest import Client
from Hotel import Hotel 
from customer import Customer
from datetime import datetime
from reservations import Reservations
# Hotels info list [hotel number ,hotel name , city , total room , empty room]
'''hotel_list = [[1,"hotel_A","jordan",50,25],
			[2,"hotel_B","sauida arabia",100,0],
			[3,"hotel_C","jordan",150,100]]'''
# Customers list
'''cust_list = [["lujian", "+962797820291"], ["kareem", "+966583116531"],["kinan" , "+962795613725"]]'''
# Reservation list [hotel number,customer number,reservation from date,reservation to date]
'''reservation_list = [[1, 2 , 28/05/2018 , 30/05/2018],
					[1,1,05/05/2018,10/05/2018],
					[2,1,01/05/2018,20/05/2018],
					[3,3,06/05/2018,25/05/2018]]'''
# Add new hotel
'''def add_hotel(number,hotel_name,city,total_rooms,empty_rooms):
	if hotel_name in hotel_list:
		print "This hotel in in the list"
	else:
		hotel_list.append([number,hotel_name,city,total_rooms,empty_rooms])'''
# add new customer
'''def add_customer(customer_name):
	if customer_name in cust_list:
		print "This customer is in the list"
	else:
		cust_list.append(customer_name)'''


	#else:
	#	print "sorry no rooms avaliable"
'''def list_hotels_in_city(city_name):
	hotels_list = []
	for e in hotel_list:
		if e[2] == city_name:
			hotels_list.append([e[1],str(e[3])+" room"])
	if hotels_list == []:
		print "There is no hotels in " + city_name
	else:
		print "In "+ city_name + " there is " + str(hotels_list)'''
'''def list_resevrations_for_hotel(hotel_name):
	cl = []
	for e in hotel_list:
		if e[1] == hotel_name:
			Hotel_num = e[0]
	for i in reservation_list:
		if i[0] == Hotel_num:
			if i[1]-1 < len(cust_list):
				cl.append(cust_list[i[1]-1])
	print "There is " + str(cl) + "in " + hotel_name'''
# Send message for customer
'''def send_text_message(message, number):
	account_sid = "ACde86f6f31ac92acadc62ca667fabe720"
# Your Auth Token from twilio.com/console
	auth_token  = "b92e6e71120f84bbdcc2fb80f349e4ba" #who i am

	client = Client(account_sid, auth_token)	

	message = client.messages.create(
    	to=number,
    	from_="+19592084162",
    	body=message)'''


#list_hotels_in_city("jordan")
#new_hotel = Hotel(1,"hotel_A","jordan",50,25)
new_hotel2 = Hotel(1,"hotel_A","jordan",50,25)
new_hotel2.list_hotels_in_city(new_hotel2.city)
#new_hotel.add_hotel(1,"hotel_A","jordan",50,25)
#print new_hotel1.name
#new_hotel.list_hotels_in_city(new_hotel.city)
new_customer = Customer("lujain" , "+962797202891")
print new_customer.PhoneNum

new = Reservations()
new.add_new_reservation("hotel_A", "lujain" ,"+962795613725", 28/05/2018 , 30/05/2018)
new.list_resevrations_for_hotel("hotel_A")

