import sys

# Definición de tipos para mayor claridad (Typing)
from typing import Final

# Constantes Globales (Clean Code: Evita números mágicos)
TASA_CAMBIO_USD: Final[float] = 3.75

class CurrencyConverter:
    """Clase encargada de la lógica de negocio para conversión de divisas."""

    @staticmethod
    def soles_to_dollars(amount: float, rate: float = TASA_CAMBIO_USD) -> float:
        """
        Realiza la conversión de Soles a Dólares.
        Raises:
            ValueError: Si el monto o la tasa son negativos.
        """
        if amount < 0 or rate <= 0:
            raise ValueError("El monto y la tasa deben ser valores positivos.")
        return round(amount / rate, 2)

def run_app():
    """Punto de entrada de la aplicación y manejo de interfaz de usuario."""
    print(f"--- Sistema de Conversión de Divisas | Tasa: {TASA_CAMBIO_USD} ---")

    try:
        # Captura de datos con tipado flotante
        raw_input = input("Ingrese el monto en Soles (S/): ").strip()
        soles_amount = float(raw_input)

        # Invocación de la lógica de conversión
        result = CurrencyConverter.soles_to_dollars(soles_amount)

        # Output formateado con f-strings
        print(f"Resultado: {soles_amount:.2f} PEN -> {result:.2f} USD")

    except ValueError as e:
        # Manejo específico de errores de conversión de tipo o lógica
        print(f"Error de validación: Entrada no permitida o monto inválido.")
        sys.exit(1)
    except Exception as e:
        # Captura de errores inesperados para evitar el cierre abrupto (Crash)
        print(f"Error inesperado en el sistema: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_app()