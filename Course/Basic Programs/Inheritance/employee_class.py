class Employee:

    salary = 1000
    increment = 1.5

    @property 
    def totalSalary(self):
        return self.salary*self.increment

    @totalSalary.setter
    def totalSalary(self,total):
        self.increment = total/self.salary

bilal = Employee()

print(bilal.increment)
print(bilal.totalSalary)

bilal.totalSalary = 2000
print(bilal.increment)