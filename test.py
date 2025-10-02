import unittest
from main_v1 import calculate_cost

class TestShippingCost(unittest.TestCase):

    # Test cases từ bảng quyết định
    def test_T1(self):
        with self.assertRaises(ValueError):
            calculate_cost(0, "Nội thành")

    def test_T2(self):
        with self.assertRaises(ValueError):
            calculate_cost(0, "Ngoại thành")

    def test_T3(self):
        self.assertEqual(calculate_cost(50, "Nội thành"), 250000)

    def test_T4(self):
        self.assertEqual(calculate_cost(50, "Ngoại thành"), 400000)

    def test_T5(self):
        self.assertEqual(calculate_cost(200, "Nội thành"), 2000000)

    def test_T6(self):
        self.assertEqual(calculate_cost(200, "Ngoại thành"), 4000000)

    def test_T7(self):
        with self.assertRaises(ValueError):
            calculate_cost(1001, "Nội thành")

    def test_T8(self):
        with self.assertRaises(ValueError):
            calculate_cost(1001, "Ngoại thành")

    # Test cases từ giá trị biên
    def test_B1(self):
        self.assertEqual(calculate_cost(100, "Nội thành"), 1000000)

    def test_B2(self):
        self.assertEqual(calculate_cost(100, "Ngoại thành"), 2000000)

    def test_B3(self):
        self.assertEqual(calculate_cost(1, "Nội thành"), 5000)

    def test_B4(self):
        self.assertEqual(calculate_cost(2, "Nội thành"), 10000)

    def test_B5(self):
        self.assertEqual(calculate_cost(1000, "Nội thành"), 10000000)

    def test_B6(self):
        self.assertEqual(calculate_cost(999, "Nội thành"), 9990000)


if __name__ == "__main__":
    unittest.main()
