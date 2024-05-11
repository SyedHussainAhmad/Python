class Employee:
    company = "Microsoft"
    def printSalary(self):
        print (f'The salary of {self.name} working in {self.company} is {self.salary}.')

hussain  = Employee()
hussain.name = 'Hussain'
hussain.salary = '100K'
hussain.printSalary()