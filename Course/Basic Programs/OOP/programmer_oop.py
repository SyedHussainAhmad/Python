class Programmer:
    company = 'Microsoft'
    def printData(self):
        print(f'The Employee name is {self.name}.')
        print (f'The salary of {self.name} is {self.salary}.')
        print (f'The Positin of {self.name} is {self.position}.')


hussain = Programmer()
bilal = Programmer()
ahmed = Programmer()
shaheer = Programmer()

hussain.name = 'Hussain'
bilal.name = 'Bilal'
ahmed.name = 'Ahmed'
shaheer.name = 'Shaheer'

hussain.salary = 100
bilal.salary = 90
ahmed.salary = 80
shaheer.salary = 70

hussain.position =  'CEO'
bilal.position =  'CPO'
ahmed.position =  'General Manager'
shaheer.position =  'Manager'

hussain.printData()
bilal.printData()
ahmed.printData()
shaheer.printData()