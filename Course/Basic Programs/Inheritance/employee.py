class Employee:
    company = "Google"
    def getResult(self):
        print(f'{self.name} is an Employee of {self.company}.')

class Programmer (Employee):
    language = 'Python'
    def showLang(self):
        print (f'The language used by {self.name} is {self.language}.')

    def getResult(self):
        print(f'{self.name} is a Programmer at {self.company}.')


bilal  = Employee()
ahmed= Programmer()

bilal.name = 'Bilal'
ahmed.name = 'Ahmed'

bilal.getResult()
ahmed.getResult()
ahmed.showLang()
