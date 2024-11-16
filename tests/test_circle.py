import unittest
from circle import area, perimeter
import math


class TestCircle(unittest.TestCase):

    def test_area(self):
        # Arrange (given)
        radius = 1

        # Act (when)
        result = area(radius)

        # Assert (then)
        self.assertAlmostEqual(result, math.pi, places=7)

    def test_area_zero(self):
        # Arrange (given)
        radius = 0

        # Act (when)
        result = area(radius)

        # Assert (then)
        self.assertEqual(result, 0)

    def test_perimeter(self):
        # Arrange (given)
        radius = 1

        # Act (when)
        result = perimeter(radius)

        # Assert (then)
        self.assertAlmostEqual(result, 2 * math.pi, places=7)

    def test_perimeter_zero(self):
        # Arrange (given)
        radius = 0

        # Act (when)
        result = perimeter(radius)

        # Assert (then)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
