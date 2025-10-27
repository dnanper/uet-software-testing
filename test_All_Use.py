import unittest
from main_v1 import calculate_cost 

class TestShippingCost(unittest.TestCase):

    def test_T1(self):
        with self.assertRaises(ValueError):
            calculate_cost(0, "A")

    def test_T2(self):
        result = calculate_cost(1, "nội thành")
        self.assertEqual(result, 5000)

    def test_T3(self):
        result = calculate_cost(100, "nội thành")
        self.assertEqual(result, 1000000)

    def test_T4(self):
        result = calculate_cost(1, "ngoại thành")
        self.assertEqual(result, 8000)

    def test_T5(self):
        result = calculate_cost(100, "ngoại thành")
        self.assertEqual(result, 2000000)

    def test_T6(self):
        with self.assertRaises(ValueError):
            calculate_cost(1, "A")

if __name__ == "__main__":
    unittest.main()

