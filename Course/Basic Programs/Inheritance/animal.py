class Animal:
    animalType = 'Mamal'
    animalBehavior = 'wild'

    def getBehavior(self):
        if self.animalBehavior is 'wild':
            print (f'The animal is {self.animalBehavior} so generally it is not a pet.')

        elif self.animalBehavior is 'mild':
            print (f'The animal is {self.animalBehavior} it can be a pet but it is not recommended.')
        
        elif self.animalBehavior is 'peaceful':
            print (f'The animal is {self.animalBehavior} and suitable to be pet.')


class Pets(Animal):
    animalBehavior = 'peaceful'    

    def nickName(self,nick):
        self.nickname = nick
        print (f'The nickname of your pet is {self.nickname}.')
        
class Dog(Pets):
    color = 'White'
    breed = 'Shepherd Dog'

    @staticmethod
    def bark():
        print ('As it is a Dog, It barks Bow Bow!!')


duke = Dog()
duke.getBehavior()
duke.nickName('Duke')
duke.bark()