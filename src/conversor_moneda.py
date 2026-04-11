import os
import sys

"""
PROYECTO: CONVERSOR DE DIVISAS PRO
ASIGNATURA: CONSTRUCCIÓN DE SOFTWARE
INTEGRANTES:
1. Saravia Chávez, Arny Rubén
2. Morales Apesteguia, Mike Nick
3. Harol Antony Porras Lume
4. Oscar Quispe, Ayma
5. Mayhualla Loayza, Jeyson Gustavo
"""

def realizar_conversion(monto, tasa):
    return round(monto * tasa, 2)

def ejecutar_interfaz():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("========================================")
    print("   SISTEMA DE CONVERSIÓN DE DIVISAS")
    print("      Universidad Continental")
    print("========================================")
    
    try:
        monto = float(input("Ingrese la cantidad a convertir: "))
        tasa_actual = 3.75  
        
        resultado = realizar_conversion(monto, tasa_actual)
        
        print(f"\nResultado final: {resultado}")
        print("========================================")
        
    except ValueError:
        print("\n[ERROR]: Ingrese un monto numérico válido.")
        sys.exit(1)

if __name__ == "__main__":
    ejecutar_interfaz()
