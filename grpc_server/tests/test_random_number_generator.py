import unittest
from ..services.random_number_generator import RandomNumberGenerator

class TestRandomNumberGenerator(unittest.TestCase):
    def test_generate_within_default_range(self):
        generator = RandomNumberGenerator()
        number = generator.generate()
        self.assertGreaterEqual(number, 1)
        self.assertLessEqual(number, 1000)

if __name__ == '__main__':
    unittest.main()
