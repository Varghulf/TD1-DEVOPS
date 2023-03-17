import math
import unittest

class TestJarod1(unittest.TestCase):
    def jarod1(self,nbSec):
        """Convertit un nombre de secondes en années, mois, jours, heures, minutes et secondes"""
        if nbSec < 0:
            raise ValueError("Le nombre de secondes doit être positif")
        nbSecRes = nbSec
        nbYr = nbSecRes // 31536000
        if nbYr > 1 :
            nbSecRes -= 31536000 * nbYr
        nbMt = nbSecRes // 2628002
        if nbMt > 1 :
            nbSecRes -= 2628002 * nbMt
        nbDay = nbSecRes // 86400
        if nbDay > 1 :
            nbSecRes -= 86400 * nbDay
        nbHour = nbSecRes // 3600
        if nbHour > 1 : 
            nbSecRes -= 3600 * nbHour
        nbMin = nbSecRes // 60
        if nbMin > 1 : 
            nbSecRes -= 60 * nbMin

        return (nbYr,nbMt,nbDay,nbHour,nbMin,nbSecRes)

    def jarod2(self,rayon):
        """Calcule le volume d'une sphère à partir de son rayon"""
        if rayon < 0:
            raise ValueError("Le rayon doit être positif")
        volume = (4 * math.pi/3) * math.pow(rayon,3)
        return volume
    
    #Implémenter les tests unitaires en utilisant le module unittest
    def testJarod1(self):
        self.assertEqual(self.jarod1(31536000), (1, 0, 0, 0, 0, 0))
        self.assertEqual(self.jarod1(2628002), (0, 1, 0, 0, 0, 0))
        self.assertEqual(self.jarod1(86400), (0, 0, 1, 0, 0, 0))
        self.assertEqual(self.jarod1(3600), (0, 0, 0, 1, 0, 0))
        self.assertEqual(self.jarod1(60), (0, 0, 0, 0, 1, 0))
        self.assertEqual(self.jarod1(10), (0, 0, 0, 0, 0, 10))
        self.assertEqual(self.jarod1(1), (0, 0, 0, 0, 0, 1))
        self.assertEqual(self.jarod1(0), (0, 0, 0, 0, 0, 0))
        self.assertEqual(self.jarod1(-1), ValueError)
        self.assertEqual(self.jarod1(-10), ValueError)
        self.assertEqual(self.jarod1(-100), ValueError)
        self.assertEqual(self.jarod1(-1000), ValueError)
        self.assertEqual(self.jarod1(-10000), ValueError)
        self.assertEqual(self.jarod1(-100000), ValueError)
        self.assertEqual(self.jarod1(-1000000), ValueError)
        self.assertEqual(self.jarod1(-100000000), ValueError)
    

if __name__ == "__main__":
    unittest.main()