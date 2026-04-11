import sys
from typing import Final

# INTEGRANTES DEL EQUIPO:
# 1. Harol Antony Porras Lume 
# 2. Arny Rúben Saravia Chavez - 74355027@continental.edu.pe
# 3. Oscar Quispe Ayma - 25001248@Scontinental.edu.pe
# 4. Mike Nick Morales Apesteguia (70177644@continental.edu.pe)
# 5. Jeyson Gustavo Mayhualla Loayza (76598227@continental.edu.pe)

TASA_CAMBIO_USD: Final[float] = 3.75

class CurrencyConverter:
    """Clase encargada de la lógica de negocio para conversión de divisas."""
    @staticmethod
    def soles_to_dollars(amount: float, rate: float = TASA_CAMBIO_USD) -> float:
        if amount < 0 or rate <= 0:
            raise ValueError("El monto y la tasa deben ser valores positivos.")
        return round(amount / rate, 2)

def run_app():
    print(f"--- Sistema de Conversión de Divisas | Tasa: {TASA_CAMBIO_USD} ---")
    try:
        soles_amount = float(input("Ingrese el monto en Soles (S/): ").strip())
        result = CurrencyConverter.soles_to_dollars(soles_amount)
        print(f"Resultado: {soles_amount:.2f} PEN -> {result:.2f} USD")
    except ValueError:
        print(f"Error de validación: Entrada no permitida o monto inválido.")
        sys.exit(1)

if __name__ == "__main__":
    run_app()
