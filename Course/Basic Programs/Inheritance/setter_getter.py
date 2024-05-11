class Teacher:
    salary = 1000
    bonus = 200

    @property
    def totalSalary(self): 
        return self.salary + self.bonus

    @totalSalary.setter
    def totalSalary(self,num):
        self.bonus= num-self.salary

sirHaider = Teacher()
print (sirHaider.totalSalary)
sirHaider.totalSalary = 2000
print (sirHaider.bonus)
print (sirHaider.totalSalary)