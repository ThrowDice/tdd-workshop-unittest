import unittest

def getPrimeList(n):
    result = []
    is_prime = 1;
    if n == 2:
        return [2]
    for i in range(2, int(n)/2+1):
        if n%i == 0:
            result.extend(getPrimeList(n/i))
            result.extend(getPrimeList(i))
            is_prime = 0;
            break
    if is_prime:
        return [n]
    else:
        return sorted(result)

class GetPrimeFactorTests(unittest.TestCase):  
    def testtwo(self):
        self.assertEqual(getPrimeList(2), [2])

    def testnine(self):
        self.assertEqual(getPrimeList(9), [3, 3])

    def test18(self):
        self.assertEqual(getPrimeList(18), [2, 3, 3])

    def test93(self):
        self.assertEqual(getPrimeList(97), [97])
    
    def test1777(self):
        self.assertEqual(getPrimeList(1777), [1777])

    def test19979(self):
        self.assertEqual(getPrimeList(199779), [3, 66593])


if __name__ == '__main__':
    #print getPrimeList(199779655)
    unittest.main()
