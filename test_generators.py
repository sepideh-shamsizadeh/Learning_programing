import unittest
import generator


class TestRangeGenerator(unittest.TestCase):
    def test_range_generator(self):
        gen = generator.range_generator(0, 10, 2)
        self.assertEqual(list(gen), [0, 2, 4, 6, 8])


if __name__ == '__main__':
    unittest.main()
