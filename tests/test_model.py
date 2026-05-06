import unittest

from calculator import add, sub, mul, div


class TestModel(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertAlmostEqual(add(2.5, 1.2), 3.7)

    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(mul(4, 3), 12)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)


if __name__ == '__main__':
    unittest.main()
