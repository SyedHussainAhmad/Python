class Employee:
    def __init__(self,name,salary,company):
        self.name = name
        self.salary = salary
        self.company = company
        print ('Hello')

    def printData(self):
        print(f'The name of the Employee is {self.name}.')
        print(f'The salary of the Employee is {self.salary}.')
        print(f'The company of the Employee is {self.company}.')

hussain = Employee('Hussain',100,'YouTube')
hussain.printData()

