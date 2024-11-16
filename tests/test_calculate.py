import unittest
from calculate import calc
import math


class TestCalculate(unittest.TestCase):

    def test_circle_area(self):
        # Arrange (given)
        fig = 'circle'
        func = 'area'
        size = [1]

        # Act (when)
        result = calc(fig, func, size)

        # Assert (then)
        self.assertAlmostEqual(result, math.pi, places=7)

    def test_square_area(self):
        fig = 'square'
        func = 'area'
        size = [1]

        result = calc(fig, func, size)

        self.assertEqual(result, 1)

    def test_triangle_area(self):
        fig = 'triangle'
        func = 'area'
        size = [3, 4, 5]

        result = calc(fig, func, size)

        self.assertEqual(result, 6)

    def test_circle_perimeter(self):
        fig = 'circle'
        func = 'perimeter'
        size = [1]

        result = calc(fig, func, size)

        self.assertAlmostEqual(result, 2 * math.pi, places=7)

    def test_square_perimeter(self):
        fig = 'square'
        func = 'perimeter'
        size = [1]

        result = calc(fig, func, size)

        self.assertEqual(result, 4)

    def test_triangle_perimeter(self):
        fig = 'triangle'
        func = 'perimeter'
        size = [3, 4, 5]

        result = calc(fig, func, size)

        self.assertEqual(result, 12)

    def test_invalid_figure(self):
        # Arrange (given)
        fig = 'hexagon'
        func = 'area'
        size = [1]

        # Act & Assert (when & then)
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_invalid_function(self):
        fig = 'circle'
        func = 'volume'
        size = [1]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_invalid_size_count(self):
        fig = 'circle'
        func = 'area'
        size = [1, 2]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_invalid_triangle(self):
        fig = 'triangle'
        func = 'area'
        size = [1, 2, 10]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)


if __name__ == '__main__':
    unittest.main()
