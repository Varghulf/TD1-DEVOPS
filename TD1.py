import unittest


class ChaineDeCaractereTest(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

#Made by Antoine Caillaud
def antoine1(a):
    if isinstance(a,tuple): 
        #AFFICHAGE
        print(a[1], a[-2])
        #AJOUT
        a += (48, )
        print(a)
        #RECHERCHE
        elementToFind = [1,2,3,4]
        for element in a:
            if elementToFind == element:
                print("trouvé!")
    else:
        print('La variable n\'est pas un tuple et ne peut donc pas être utilisé')

def antoine2(a):
    if type(a)==tuple:
        #Trouver s'il y a des doublons
        b = []
        for element in a:
            try:
                b.index(element)
                print("Y a un doublon :",element)
            except ValueError:
                b.append(element)
        #Inverser l'ordre
        reversed(a)
        print(a)
    else:
        print('La variable n\'est pas un tuple et ne peut donc pas être utilisé')

a=(4, "tuple", [1,2,3,4], True, 3.14, 4)

antoine1(a)
antoine2(a)    