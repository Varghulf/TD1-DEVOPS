import unittest


class ChaineDeCaractereTest(unittest.TestCase):
    def Baptiste(self):
        if self is str () :
            compteur = 0
            for lettre in self:
                compteur += 1

            occurence = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0,
                         "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
                         "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,
                         "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
                         "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
            for lettre in self.lower():
                occurence[lettre] += 1
            return compteur, occurence
        return False


    def BOUGY(self):
        if self is str():
            cptChar = 0
            newStr = self.lower().split(maxsplit=2)
            newStr[-1] = '$'
            print(newStr, self)
            cptChar += 1

            if len(self) < 2:
                return ""
            else:
                return self[0] + self[1] + self[-1] + self[-2], newStr
        return False


if __name__ == '__main__':
    unittest.main()