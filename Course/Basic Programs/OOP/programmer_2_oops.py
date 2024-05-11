class Programmer:
    corporation = 'Microsoft'
    def __init__(self,name,salary,product):
        self.name= name
        self.salary= salary
        self.product= product

    def printData(self):
        print (f'The salary of the {self.corporation} Programmer {self.name} is {self.salary} and product is {self.product}.')

hussain = Programmer('Hussain',100,'Skype')
bilal = Programmer('Bilal',80,'VSCode')
ahmed = Programmer('Ahmed',60,'Github')

hussain.printData()
bilal.printData()
ahmed.printData()





