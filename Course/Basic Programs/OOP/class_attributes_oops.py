class Student:
    section = 'SPB-04' # --> This is the class attribute.

hussain = Student()
bilal = Student()

print(hussain.section)
print(bilal.section)


Student.section = 'SPB-03' # --> it is used to change the section by using directly the name of the class.

print(hussain.section)
print(bilal.section)