import unittest
import math

def list_squared(m, n):
    result = []

    squares = dict((x, x**2) for x in range(m, n+1))
    def cached_square(x):
        sqr = squares.get(x, None)
        if sqr is None:
            sqr = x ** 2
            squares[x] = sqr
        return sqr

    def is_square(x):
        r = math.sqrt(s)
        return (r == int(r))

    for x in range (m, n+1):
        divisors = [1]
        if x > 1: divisors.append(x)
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                divisors.append(i)
                d = (x / i)
                if (i != d):
                    divisors.append(d)
        s = sum([cached_square(i) for i in divisors])
        if is_square(x):
            result.append([x, s])
            
    return result



class Test(unittest.TestCase):

    def test_1(self):

        self.assertEquals(list_squared(1, 250),[[1, 1],[42, 2500],[246, 84100]])

    
    def test_2(self): 
       
        self.assertEquals(list_squared(42, 250), [[42, 2500], [246, 84100]])

    def test_3(self):
        
        self.assertEquals(list_squared(250, 500), [[287, 84100]])
