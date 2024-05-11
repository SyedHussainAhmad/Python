class Vector_3D:
    def __init__(self,i,j,k) -> None:
        self.icap = i
        self.jcap = j
        self.kcap = k

    def __str__(self) -> str:
        return f'{self.icap}i+{self.jcap}j+{self.kcap}k'

vector = Vector_3D(2,3,4)
print(vector)