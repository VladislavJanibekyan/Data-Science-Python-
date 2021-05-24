class Room():
	def __init__(self,room_type,room_count):
		self.__room_type = room_type
		self.__room_count = room_count
	def get__type(self):
		return self.__room_type
	def set_type(self,room_type):
		self.__room_type = room_type
	def del_type(self):
		del self.__room_type
	room_type = property(get__type,set_type,del_type,doc="room_type")

	def __repr__(self):
		return f"room type - {self.__room_type} \nroom count - {self.__room_count}"
	def get__count(self):
		return self.__room_count
	def set_count(self,room_count):
		self.__room_count = room_count
	def del_count(self):
		del self.__room_count
	room_count = property(get__count,set_count,del_count,doc="room_count")

	def reserve(self):
		self.__room_count -= 1
		return Room(self.__room_type,self.__room_count)
	def checkout(self):
		self.__room_count += 1
		return Room(self.__room_type,self.__room_count)

class  Hotel():
	def __init__(self,rating,rater_count,room_list):
		self.__rating = rating
		self.__rater_count = rater_count
		self.room_list  = room_list
	def get_rating(self):
		return self.__rating
	def set_rating(self,rating):
		self.__rating = rating
	def del_rating(self):
		del self.__rating
	rating = property(get_rating,set_rating,del_rating,doc="rating")
	def get_rooms(self):
		for i in room_list:
			print(i)

	def rate(self):
		user_rate = int(input("rate 1-5: "))
		self.__rater_count+=1
		new_rate =  


room_1 = Room("double", 4)
room_1.reserve()

print(room_1)
room_1.checkout()
print(room_1)

