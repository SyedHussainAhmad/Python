class Teacher:
    college = 'PGC'

sirHaider= Teacher()
sirRizwan = Teacher()

sirHaider.subject = 'Computer' # --> This is an intance attribute
sirRizwan.subject = 'Maths' # --> This is an intance attribute

print (f'The subject of Sir Haider is {sirHaider.subject}.')
print (f'The subject of Sir Rizwan is {sirRizwan.subject}.')