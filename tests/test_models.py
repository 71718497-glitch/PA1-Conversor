# tests/test_database.py
import pytest
from database import SessionLocal, init_db
from models import Historial

# Opcional: Esto asegura que la base de datos se cree antes de las pruebas
def setup_module(module):
    init_db()

def test_guardar_historial():
    # 1. Configuración (Setup)
    session = SessionLocal()
    
    # 2. Ejecución (Act)
    conversion = Historial(monto_origen=100.0, monto_resultado=26.67)
    session.add(conversion)
    session.commit()

    # 3. Verificación (Assert)
    resultado = session.query(Historial).filter_by(monto_origen=100.0).first()
    
    assert resultado is not None
    assert resultado.monto_resultado == 26.67
    
    # 4. Limpieza (Teardown)
    session.close()