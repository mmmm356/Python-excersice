class Hotel: # i am defining a class
    def _int_(self, name, numberofRooms, location, services): # are parameters to be pass
        self.name = name # is an attribute the hold the name data
        self.numberofRooms = numberofRooms # is an attributs that holds numbers of Rooms
        self.location = location # is an attributs to hold location
        self.services = services # is an attributs the hold the services

        # to create a Read operation function 
        def viewHotelRooms(self):
            return f"The hotel {self.name} has {self.numbersofRooms} rooms"
        
        def viewHotelRooms(self):
            return f"The hotel {self.name} is in {self.location}"
        

        # creating an object based on the class 
        object_1 = Hotel("Elian",150, "Addis Ababa", "swimming pool, spa, meeting hall" )
        object_2 = Hotel("sheraton", 1500, "Addis Ababa", "spa, meetin hall")

        print(object_1.viewHotelRooms())
        