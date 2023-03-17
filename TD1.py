import math
import unittest

class ChaineDeCaractereTest(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(True)


def thomas():
    #EXERCICE 3.1
    def mul7():
        for i in range(1,21):
            if (7*i)%3==0:
                print(7*i,"*")
            else:
                print(7*i)

    mul7()

    #EXERCICE 3.2
    def mul13():
        for i in range(1,51):
            if (13 * i) % 7 == 0:
                print(13*i)
    mul13()
    cottigny()


def cottigny():
        #EXERCICE 2.1
    def determinationMax(a,b,c):
        if a >= b >= c or a >= c >= b:
            return a
        elif b >= a >= c or b >= c >= a:
            return b
        elif c >= a >= b or c >= b >= a:
            return c
        
    print(determinationMax(6, 6, 2))

    #EXERCICE 2.5
    def deterTriangle():
        a = input("Saisissez la valeur pour a ")
        b = input("Saisissez la valeur pour b ")
        c = input("Saisissez la valeur pour c ")
        try:
            val = int(a), int(b), int(c)
            print("La valeur entree est un entier = ", val)
            
            if determinationMax(a, b, c) == a:
                if (math.pow(a,2) == math.pow(b,2) + math.pow(c,2)) and (c == b or a == b or a == c):
                    print("Le triangle est rectangle et isocèle")
                elif math.pow(a, 2) == math.pow(b, 2) + math.pow(c, 2):
                    print("Le triangle est rectangle")
                elif c == b and a == b and a == c:
                    print("Le triangle est équilatéral")
                elif c == b or a == b or a == c:
                    print("Le triangle est isocèle")
                else:
                    print("Le triangle est quelconque")
            elif determinationMax(a, b, c) == b:
                if (math.pow(b,2) == math.pow(a,2) + math.pow(c,2)) and (c == b or a == b or a == c):
                    print("Le triangle est rectangle et isocèle")
                elif math.pow(b, 2) == math.pow(a, 2) + math.pow(c, 2):
                    print("Le triangle est rectangle")
                elif c == b and a == b and a == c:
                     print("Le triangle est équilatéral")
                elif c == b or a == b or a == c:
                    print("Le triangle est isocèle")
                else:
                    print("Le triangle est quelconque")
            elif determinationMax(a, b, c) == c:
                if (math.pow(c,2) == math.pow(b,2) + math.pow(a,2)) and (c == b or a == b or a == c):
                    print("Le triangle est rectangle et isocèle")
                elif math.pow(c, 2) == math.pow(b, 2) + math.pow(a, 2):
                    print("Le triangle est rectangle")
                elif c == b and a == b and a == c:
                    print("Le triangle est équilatéral")
                elif c == b or a == b or a == c:
                    print("Le triangle est isocèle")
                else:
                    print("Le triangle est quelconque")
        except ValueError:
            print("Ce n'est pas un entier!")
    
    deterTriangle()
thomas()
cottigny()


if __name__ == '__main__':
    unittest.main()