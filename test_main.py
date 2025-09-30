import unittest 
from main import fizzbuzz
from main import factorial

#fizzbuzz test cases:
result = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
class TestMethods(unittest.TestCase):
    
    #test case 1: input is 3, expected output is "[1,2,'fizz']"
    def test_fizz(self):
        
        self.assertEqual(fizzbuzz(3), result[:3])
    
    #test case 2: input is 5, expected output is "[1,2,'fizz',4,'buzz']"
    def test_Buzz(self):
        self.assertEqual(fizzbuzz(5), result[:5])

    #test case 3: input is 15, expected output is full list]
    def  test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), result)
   
    #test case 4: input is 7, expected output is [1,2,'fizz',4,'buzz','fizz',7]
    def test_fizzNum(self):
        self.assertEqual(fizzbuzz(7), result[:7])
        

    #factorial test cases:
    
    #test case 1: input is negative, expected output is ValueError
    def test_negative(self):    
        with self.assertRaises(ValueError):
            factorial(-5)
        

    #test case 2 : input is 0, expected output is 1
    def test_zero(self):
        self.assertEqual(factorial(0), 1)
    
    #test case 3: input is 1, expected output is 1
    def test_one(self):     
        self.assertEqual(factorial(1), 1)
    
    #test case 4: input is 5, expected output is 120
    def test_five(self):                
        self.assertEqual(factorial(5), 120)

    #test case 5: input is 10, expected output is 3628800
    def test_ten(self):     
        self.assertEqual(factorial(10), 3628800)
    

if __name__ == '__main__':
    unittest.main()