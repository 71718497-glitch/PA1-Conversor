import pytest
from src.conversor_moneda import realizar_conversion


def test_conversion_exitosa():
    # Prueba básica: 10 * 3.75 = 37.5
    assert realizar_conversion(10, 3.75) == 37.5


def test_conversion_cero():
    # Prueba con cero: 0 * 3.75 = 0.0
    assert realizar_conversion(0, 3.75) == 0.0


def test_conversion_decimales():
    # Prueba con decimales: 10.5 * 2.0 = 21.0
    assert realizar_conversion(10.5, 2.0) == 21.0
