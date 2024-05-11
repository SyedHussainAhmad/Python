def names (*args,**kwargs):
    for item in args:
        print(item)

    for key,value in kwargs.items():
        print(f"{key} is {value}.")

list = ["Hussain","Bilal"]
dict = {"Programmer":"Debugger"}
names(*list,**dict)