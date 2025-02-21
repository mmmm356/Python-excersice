class Hotel:
    def  __init__(self, name,location, rooms):
    #Initialize the hotel with a name , location, and number of room
         self.name = name   # Hotel name
         self.location = location  # Hotel location
         self.rooms = rooms       #Total numbers of rooms
         self.booked_rooms = 0    # Rooms currently booked

    # book info create operation
    def book_room(self, numbers_of_rooms):
            # Book a specified number of rooms.
        if numbers_of_rooms <=0:
            print("Number of rooms to book must be positive.")
            return
        
        if self.booked_rooms + numbers_of_rooms > self.rooms: # available room
            print("not enougn available rooms to book.")
            return
        
        self.booked_rooms += numbers_of_rooms
        print(f"{numbers_of_rooms} room(s) successfully booked.")

       # book info delete operation 
    def checkout(self, number_of_rooms):
        # """"check out a specified number of rooms.""""
        if number_of_rooms <= 0:
            print("numbers of rooms to checkout must be postive.")
            return
        if number_of_rooms > self.booked_rooms:
            print("cannot checkout more rooms than booked.")
            return
         

        self.booked_rooms -= number_of_rooms
        print(f"{number_of_rooms} room(s) successfully checked out.")

    def get_availability(self):  
        '''get the nuber of available rooms.'''
        available_rooms = self.rooms = self.booked_rooms
        return available_rooms
    def _str_(self):
        """Return a string representation of the hotel ."""
        return f"Hotel: {self.name}, location: {self.location}, Total Rooms: {self.room}, booked rooms: {self.bookedrooms}"
    

# creating an object of the hotel class
my_hotel = Hotel("seaside resort", "california", 20)

# Accessing attributes and methods 
print(my_hotel) # Display hotel details 

# booking rooms
my_hotel.book_room(22)
print(f"available rooms: {my_hotel.get_availability()}") # check availabe

# checking out rooms
my_hotel.checkout(4)
print(f"Available rooms: {my_hotel.get_availability()}") # check available
