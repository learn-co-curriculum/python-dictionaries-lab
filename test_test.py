import unittest2 as unittest
from ipynb.fs.full.index import (greenville, greenville_population, area, city_keys, city_values, cities, salina, los_cabos_pop, city_count, pyeongchang_keys, pyeongchang_values)

class TestDictionary(unittest.TestCase):
    def test_greenville_population(self):
        self.assertEqual(greenville_population, 84554)

    def test_area(self):
        self.assertEqual(area, 68)

    def test_city_keys(self):
        self.assertEqual(city_keys, ['Area', 'City', 'Country', 'Population'])

    def test_city_values(self):
        self.assertEqual(city_values, [68, 'Greenville', 'USA', 84554])

    def test_salina(self):
        self.assertEqual(salina, {'Area': 27, 'City': 'Salina Island', 'Country': 'Italy', 'Population': 4000})

    def test_los_cabos_pop(self):
        self.assertEqual(los_cabos_pop, 287651)

    def test_city_count(self):
        self.assertEqual(city_count, 12)

    def test_change_spelling(self):
        self.assertEqual(cities[11]['City'], 'PyeongChang')

    def test_pyeongchang_keys(self):
        self.assertEqual(pyeongchang_keys, ['PyeongChang', 'South Korea', 2581000, 3194])
        self.assertEqual(type(pyeongchang_keys), type(list()))

    def test_pyeongchang_values(self):
        self.assertEqual(pyeongchang_values, ['City', 'Country', 'Population', 'Area'])
        self.assertEqual(type(pyeongchang_values), type(list()))
