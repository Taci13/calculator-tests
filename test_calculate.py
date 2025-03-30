import unittest  
from calculator import calculate  

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        expression = "4 + 5"
        expected_result = 9
        actual_result = calculate(expression)  
        self.assertEqual(expected_result, actual_result)

    def test_operator_precedence(self):
        expression = "10 + 5 * 4 + 3"
        expected_result = 33  
        actual_result = calculate(expression)
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main() 