import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
      self.assertEqual(calc.add(10,5),15)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(1,-1),2)

    def test_multiply(self):

        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-1,-1),1)
        self.assertEqual(calc.multiply(-1,1),-1)
    
    def test_divide(self):

        self.assertEqual(calc.divide(10,5),2) 
        with self.assertRaises(ValueError):
            calc.divide(10,0)

if __name__ == '__main__':
    unittest.main()