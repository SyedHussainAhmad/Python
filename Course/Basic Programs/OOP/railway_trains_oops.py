class Train:
    def __init__(self,name,fare,seats):
        self.name= name
        self.fare = fare
        self.seats = seats

    def statusInfo(self):
        print(f'The name of the train is {self.name}.')
        print(f'The seats available in the train is {self.seats}.')
    
    def fareInfo(self):
        print(f'The fare of the train is Rs {self.fare}.')

    def bookMethods(self):
        if self.seats>0:
            print(f"Your booking is confirmed and your seat number is {self.seats}. ")
            self.seats= self.seats-1
        else:
            print('Sorry the train is full.Your request cannot be fulfilled.')
        



travel = Train('Subuk Khuram',650,280)
travel.bookMethods()
travel.statusInfo()
travel.fareInfo()

