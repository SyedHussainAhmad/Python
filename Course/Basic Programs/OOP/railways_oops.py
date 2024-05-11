class RailwayForm:
    formType = 'RailwayForm'
    def printData(self):
        print(f'Name is {self.name}')
        print(f'Train is {self.train}')
        print(f'Train Timing is {self.train_timing}')
        print(f'Date of Arrival is {self.date}')

hussain_Application = RailwayForm()
hussain_Application.name = input("Enter name\n")
hussain_Application.train = "Subak Khuram."
hussain_Application.train_timing = '7:30.'
hussain_Application.date = '1-Jan-2022.'
hussain_Application.printData()