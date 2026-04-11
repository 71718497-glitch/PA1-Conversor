import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from conversor_moneda import realizar_conversion

class TestConversor(unittest.TestCase):

    def test_operacion_basica(self):
        self.assertEqual(realizar_conversion(10, 3.75), 37.5)

    def test_monto_cero(self):
        self.assertEqual(realizar_conversion(0, 3.75), 0.0)

if __name__ == '__main__':
    unittest.main()
