class Calculator:
    @staticmethod
    def greet():
        print('Hello Here are your desired results. ')

    def __init__(self,num):
        self.number=num
    
    def square(self):
        print(f'The square of {self.number} is {self.number **2}.')

    def cube(self):
        print(f'The cube of {self.number} is {self.number **3}.')

    def squareRoot(self):
        print(f'The square root of a {self.number} is {self.number **0.5}.')


a = int(input('Enter any number for desired calculations\n'))
b = Calculator(a)

b.greet()
b.square()
b.cube()
b.squareRoot()
