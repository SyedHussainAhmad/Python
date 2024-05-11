class GrandPa:
    country = 'Pakistan'
    city = 'Lahore'
    beard = True
    automobile = 'Scooter'

    def __init__(self):
        print('Hello Grandpa')

    def printBeard(self):
        if self.beard is True:
            print(f'{self.name} have a beard.')
        else:
            print(f'{self.name} do not have a beard.')

    def autoMobile(self):
        if self.automobile is 'scooter':
            print(f"The {self.name} belongs to 40's")
        elif self.automobile is 'bike':
            print(f"The {self.name} belongs to 60's")
        else:
            print(f"The {self.name} belongs to new generation")


class Father(GrandPa):
    country = "Dubai"
    beard = False
    automobile = 'bike'

    def __init__(self):
        super().__init__()
        print('Hello Father')


class GrandSon(Father):

    city = 'Islamabad'
    beard = False
    automobile = 'Tesla'

    def __init__(self):
        super().__init__()
        print('Hello Grandson')


gP = GrandPa()
f = Father()
gS = GrandSon()

gP.name = 'DADA'
f.name = 'BABA'
gS.name = 'POTA'

gS.printBeard()
gS.autoMobile()
