class Railway:
    # def __init__(self):
    #     pass
    def printData(self):
        print (f'You can book tickets by the methods which are {self.methods}.The no of seats are booked by {self.name} are {self.status} and the fare for each ticket is {self.fare}. ')

ticket = Railway()
ticket.name = 'Hussain'
ticket.methods = 'Online and Offline'
ticket.status = '3'
ticket.fare= 650
ticket.printData()