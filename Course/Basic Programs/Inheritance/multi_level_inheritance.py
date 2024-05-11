class GrandPa:
    country = 'Pakistan'
    city = 'Lahore'
    beard = True

    def printBeard(self):
        if self.beard is True:
            print (f'{self.name} have a beard.')
        else:
            print (f'{self.name} do not have a beard.')


class Father(GrandPa):
    beard = False

class GrandSon(Father):
    city = 'Islamabad'
    beard = False

gP= GrandPa()
f= Father()
gS= GrandSon()

gP.name = 'DADA'
f.name = 'BABA'
gS.name = 'POTA'

gS.printBeard()