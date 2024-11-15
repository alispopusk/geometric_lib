import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):

    def test_area(self):
        # Arrange (given)
        side = 1

        # Act (when)
        result = area(side)

        # Assert (then)
        self.assertEqual(result, 1)

    def test_area_zero(self):
        # Arrange (given)
        side = 0

        # Act (when)
        result = area(side)

        # Assert (then)
        self.assertEqual(result, 0)

    def test_perimeter(self):
        # Arrange (given)
        side = 1

        # Act (when)
        result = perimeter(side)

        # Assert (then)
        self.assertEqual(result, 4)

    def test_perimeter_zero(self):
        # Arrange (given)
        side = 0

        # Act (when)
        result = perimeter(side)

        # Assert (then)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
