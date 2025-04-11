import unittest
from triangle import Triangle

class TestTriangle(unittest.TestCase):

    def test_perimeter(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.perimeter(), 12)

    def test_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_invalid_triangle(self):
        triangle = Triangle(1, 2, 5)
        self.assertIsNone(triangle.perimeter())
        self.assertIsNone(triangle.area())

if __name__ == '__main__':
    unittest.main()