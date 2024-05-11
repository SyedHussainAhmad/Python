class Employee:
    company = 'Microsoft'
    employeeId = 1234

class Freelancer:
    company = 'Fiverr'
    level = 0

    def updateLevel(self):
        self.level = self.level + 1
        print (f'The level of {self.name} is {self.level}')

class Programmer(Freelancer,Employee):
    def printInfo(self):
            print (f'The name of the Programmer working in {self.company} is {self.name}')

bilal = Programmer()
bilal.name = 'Bilal'
print(bilal.company)
bilal.updateLevel()