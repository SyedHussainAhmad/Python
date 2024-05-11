class Vector:
    def __init__(self,vec):
        self.vec = vec

    def __str__(self) -> str:
        str1 =''
        index = 0
        for i in self.vec:
            str1 += f'{i}a{index} +'
            index +=1
        return str1[:-1]

    def __add__(self,vec2):
            newlist=[]
            for i in range(len(self.vec)):
                newlist.append(self.vec[i] + vec2.vec[i] )
            return Vector(newlist)


    def __mul__(self,vec2):
            sum = 0
            for i in range(len(self.vec)):
                sum += self.vec[i] * vec2.vec[i]  
            return sum


dim = int(input('How many dimensions of vectos do you want.\n'))

def list1():
    list1 = []
    print('Now Enter Dimensions of first vector\n')
    for i in range (dim):
        value1 = int(input(f'Enter {i} Dimension.\n'))
        list1.append(value1)
    return list1

def list2():
    list2 = []
    print('Now Enter Dimensions of Second vector\n')
    for i in range (dim):
        value2 = int(input(f'Enter {i} Dimension.\n'))
        list2.append(value2)
    return list2

a= list1()
b= list2()

v1 = Vector(a)
v2 = Vector(b)

print (f'The First vector is {v1}.')
print (f'The Second vector is {v2}.\n')

print (f'The sum of vectors is {v1 + v2}')
print (f'The dot product of vectors is {v1 * v2}.')