from twilio.rest import Client

# Hotels info list [hotel number ,hotel name , city , total room , empty room]
hotel_list = [[1,"hotel_A","jordan",50,25],
			[2,"hotel_B","sauida arabia",100,0],
			[3,"hotel_C","jordan",150,100]]
# Customers list
cust_list = [["lujian", "+962797820291"], ["kareem", "+966583116531"],["kinan" , "+962795613725"]]
# Reservation list [hotel number,customer number,reservation from date,reservation to date]
reservation_list = [[1, 2 , 28/5/2018 , 30/5/2018],
					[1,1,5/5/2018,10/5/2018],
					[2,1,1/5/2018,20/5/2018],
					[3,3,6/5/2018,25/5/2018]]
# Add new hotel
def add_hotel(number,hotel_name,city,total_rooms,empty_rooms):
	if hotel_name in hotel_list:
		print "This hotel in in the list"
	else:
		hotel_list.append([number,hotel_name,city,total_rooms,empty_rooms])
# add new customer
def add_customer(customer_name):
	if customer_name in cust_list:
		print "This customer is in the list"
	else:
		cust_list.append(customer_name)
# add reserve room
def reserve_room(hotel_name,customer_name):
	hotel_num = 0
	for e in hotel_list:
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
def add_new_reservation(hotel_name , customer_name, Cust_number):
	hotel_num = 0
	if reserve_room(hotel_name , customer_name):
		for e in hotel_list:
			if e[1] == hotel_name:
				hotel_num = e[0]
		cust_list.append([customer_name , Cust_number])
		cust_num = len(cust_list)
		reservation_list.append([hotel_num,cust_num])
		send_text_message("Your reservation done , Thank you "+customer_name,Cust_number)
		print "Done !"
	#else:
	#	print "sorry no rooms avaliable"
def list_hotels_in_city(city_name):
	hotels_list = []
	for e in hotel_list:
		if e[2] == city_name:
			hotels_list.append([e[1],str(e[3])+" room"])
	if hotels_list == []:
		print "There is no hotels in " + city_name
	else:
		print "In "+ city_name + " there is " + str(hotels_list)
def list_resevrations_for_hotel(hotel_name):
	cl = []
	for e in hotel_list:
		if e[1] == hotel_name:
			Hotel_num = e[0]
	for i in reservation_list:
		if i[0] == Hotel_num:
			if i[1]-1 < len(cust_list):
				cl.append(cust_list[i[1]-1])
	print "There is " + str(cl) + "in " + hotel_name
# Send message for customer
def send_text_message(message, number):
	account_sid = "ACde86f6f31ac92acadc62ca667fabe720"
# Your Auth Token from twilio.com/console
	auth_token  = "b92e6e71120f84bbdcc2fb80f349e4ba" #who i am

	client = Client(account_sid, auth_token)	

	message = client.messages.create(
    	to=number,
    	from_="+19592084162",
    	body=message)


list_hotels_in_city("jordan")
