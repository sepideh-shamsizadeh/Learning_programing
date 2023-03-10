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


class TestFilterGenerator(unittest.TestCase):
    def test_fibonacci_generator(self):
        gen = generator.filter_generator(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
        self.assertEqual(list(gen), [2, 4, 6])


class TestFlattenGenerator(unittest.TestCase):
    def test_flatten_generator(self):
        gen = generator.flatten_generator([(1, 2), [3, 4], [5, [6, 7]]])
        self.assertEqual(list(gen), [1, 2, 3, 4, 5, 6, 7])


class TestPrimeGenerator(unittest.TestCase):
    def test_prime_generator(self):
        gen = generator.prime_generator(20)
        self.assertEqual(list(gen), [2, 3, 5, 7, 11, 13, 17, 19])


if __name__ == '__main__':
    unittest.main()
