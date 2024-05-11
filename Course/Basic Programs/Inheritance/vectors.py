class C2DVector:
    def __init__(self,i,j):
        self.iCap = i
        self.jCap = j
        print (f'The 2D position of the vector is ({self.iCap},{self.jCap}).')  
        print (f'The 2D vector is {self.iCap}i+{self.jCap}j.')

class C3DVector(C2DVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kCap = k
        print (f'The 3D position of the vector is ({self.iCap},{self.jCap},{self.kCap}).')  
        print (f'The 3D vector is {self.iCap}i+{self.jCap}j+{self.kCap}k.')
        
        
vector2D = C2DVector(6,9)
vector3D = C3DVector(2,3,4)

