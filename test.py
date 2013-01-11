# coding: utf-8
import unittest
import triangle


class TriangleTestCase(unittest.TestCase):

    def test_should_be_an_triangule(self):
        self.assertIsFalse(triangle.is_triangle((10, 20, 15)))
        self.assertIsFalse(triangle.is_triangle((20, 10, 12)))
        self.assertIsFalse(triangle.is_triangle((2, 4, 6)))

    def test_should_not_be_an_triangule(self):
        self.assertIsTrue(triangle.is_triangle((10, 20, 2)))
        self.assertIsTrue(triangle.is_triangle((20, 10, 2)))
        self.assertIsTrue(triangle.is_triangle((2, 4, 8)))

    def test_triangule_area(self):
        triangle_test = (2, 4, 5)
        area = triangle.calculate_area(triangle_test)

        self.assertEquals(area, 4)
