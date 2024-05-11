class Employee:
    company = 'Infinix'
    salary = 100  

    @classmethod
    def changeSalary(cls,new):
        print (f'The old salary is {cls.salary}.')
        cls.salary = new
        print(f'The new salary is {cls.salary}.')

bilal = Employee()
bilal.changeSalary(20)