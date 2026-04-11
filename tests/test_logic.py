import unittest

def calcular_cambio(monto, tasa):
    return monto * tasa

class TestSimple(unittest.TestCase):
    def test_operacion(self):
        self.assertEqual(calcular_cambio(10, 3.75), 37.5)
