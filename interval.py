import unittest


def isInInterval(a, b, n):
    if n < a :
        return False
    if n > b :
        return False
    return True

class IntervalTester(unittest.TestCase):  
    def testInInterval(self):
        self.assertTrue(isInInterval(2, 6, 3))
   
    def testBiggerThanRightBound(self):
        self.assertFalse(isInInterval(2, 6, 7))

    def testSmallerThanLeftBound(self):
        self.assertFalse(isInInterval(2, 6, 1))

    def testEqualToRightBound(self):
        self.assertTrue(isInInterval(2,6,6))

    def testEqualToLeftBound(self):
        self.assertTrue(isInInterval(2,6,2))



if __name__ == '__main__':
    #print getPrimeList(199779655)
    unittest.main()

