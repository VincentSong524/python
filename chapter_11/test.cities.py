import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """测试 city_functions.py"""
    
    def test_city_country(self):
        """能够正确处理 City, Country这样的格式吗"""
        formatted_name = city_country('city', 'country')
        self.assertEqual(formatted_name, 'City, Country')

    def test_city_population(self):
        """"能够正确处理 City, Country - population xxx 这样的格式吗"""
        formatted_name = city_country('city', 'country', '5000000')
        self.assertEqual(formatted_name, 'City, Country - population 5000000')

if __name__ == '__main__':
    unittest.main()