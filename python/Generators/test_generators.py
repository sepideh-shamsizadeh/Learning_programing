import unittest
from python.Generators import generator


class TestRangeGenerator(unittest.TestCase):
    def test_range_generator(self):
        gen = generator.range_generator(0, 10, 2)
        self.assertEqual(list(gen), [0, 2, 4, 6, 8])

class TestFibonacciGenerator(unittest.TestCase):
    def test_fibonacci_generator(self):
        gen = generator.fibonacci_generator(8)
        self.assertEqual(list(gen), [0, 1, 1, 2, 3, 5, 8, 13, 21])


if __name__ == '__main__':
    unittest.main()
