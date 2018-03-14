import unittest2 as unittest
from ipynb.fs.full.index import (greenville, greenville_population, city_values)

class TestDictionary(unittest.TestCase):
    def test_greenville_population(self):
        self.assertEqual(greenville_population, 84554)
