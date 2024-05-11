# Formula = (ac-bd)(ad+bc)i

class Complex:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i

    def __add__(self,c):
        return Complex(self.real+c.real,self.imaginary+c.imaginary)

    def __str__(self) -> str:
        return f'{self.real} + {self.imaginary}i'
    
    def __mul__(self,c):
        mulReal = self.real*c.real-self.imaginary*c.imaginary
        mulImaginary = self.real *c.imaginary + c.real*self.imaginary
        return Complex(mulReal,mulImaginary)

    def __str__(self) -> str:
        if self.imaginary < 0:
            return f'{self.real} - {-self.imaginary}i'  

        else:
            return f'{self.real} + {self.imaginary}i'   
            
a = int(input('Enter real part of First Complex Number\n'))
b = int(input('Enter imaginary part of First Complex Number\n'))
c = int(input('Enter real part of Second Complex Number\n'))
d = int(input('Enter imaginary part of Second Complex Number\n'))

c1 = Complex(a,b)
c2 = Complex(c,d)

print (f'The sum of complex numbers is {c1+c2}')
print (f'The product of complex numbers is {c1*c2}')