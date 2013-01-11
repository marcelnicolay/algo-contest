# coding: utf-8
import unittest
import algoritmo


class TriangleTestCase(unittest.TestCase):

    def test_should_be_a_triangule(self):
        self.assertTrue(algoritmo.is_triangle((10, 20, 15)))
        self.assertTrue(algoritmo.is_triangle((20, 10, 12)))
        self.assertTrue(algoritmo.is_triangle((2, 4, 6)))

    def test_should_not_be_a_triangule(self):
        self.assertFalse(algoritmo.is_triangle((10, 20, 2)))
        self.assertFalse(algoritmo.is_triangle((20, 10, 2)))
        self.assertFalse(algoritmo.is_triangle((2, 4, 8)))

    def test_triangule_area(self):
        triangle_test = (5, 10, 12)
        area = algoritmo.calculate_area(triangle_test)

        self.assertEquals(24.544602257930357, area)

    def test_triangule_area_two(self):
        triangle_test = (2, 4, 5)
        area = algoritmo.calculate_area(triangle_test)

        self.assertEquals(3.799671038392666, area)

if __name__ == '__main__':
    unittest.main()
