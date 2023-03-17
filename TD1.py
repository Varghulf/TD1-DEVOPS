import numpy as np
import unittest

def zakaria1(taille):
    
    if type(taille) != int:
        taille = 1
    if taille < 1:
        taille = 1
    
    tab = []
    for i in range(taille):
        tab.append(np.random.uniform(34,76))
    ectype = np.std(tab)
    moy = np.mean(tab)
    vpos = [i for i,x in enumerate(tab) if x>moy+1.96*ectype]
    vneg = [i for i,x in enumerate(tab) if x<moy+1.96*ectype]
    for i in vpos:
        tab[i] = max(tab)
    for i in vneg:
        tab[i] = min(tab)
    nbmax, nbmin, nbdiff = 0, 0, 0
    for i in tab:
        if i == max(tab):
            nbmax += 1
        if i == min(tab):
            nbmin += 1
        else :
            nbdiff += 1
    print(nbdiff, nbmax, nbmin)
    return(taille)

    
def zakaria2(arr):
    
    if len(arr) <= 1:
        arr[1,1]
    for i in range(len(arr)):
        if type(arr) != int:
            arr[i] = 1
        if arr[i] < 1:
            arr[i]= 1
        
    
    print(arr[::-1])
    
    i = len(arr)
    j = arr[0]

    arr = np.zeros((i,j))
    arr[:,0],arr[:,j-1],arr[0,:],arr[i-1,:] = 1,1,1,1
    print(arr)

    arr = np.zeros((8,8))
    binaire = True
    for i in range(8):
        for j in range(8):
            if binaire == True:
                if (i%2 == 0 and j%2 == 0) or (i%2 != 0 and j%2 != 0):
                    arr[i][j] = 1
    print(arr)
    return(len(arr))
    

class Testfun(unittest.TestCase):

   def test_zakaria1(self):
      self.assertAlmostEqual(zakaria1(2),2)
      self.assertAlmostEqual(zakaria1(-1),1)
      self.assertAlmostEqual(zakaria1("none"),1)

   def test_zakaria2(self):
      self.assertAlmostEqual(zakaria2([-5,2,8]),8)
      self.assertAlmostEqual(zakaria2([5,2]),8)
      self.assertAlmostEqual(zakaria2([2,2]),8)
      
if __name__ == '__main__':
    unittest.main()