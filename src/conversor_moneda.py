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

import os
import sys

def realizar_conversion(monto, tasa):
    return round(monto * tasa, 2)

def ejecutar_interfaz():
    tasa_cambio = 3.75
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("====================================")
        print("  SISTEMA DE CONVERSIÓN DE DIVISAS  ")
        print("====================================")
        print(" 1. Soles a Dólares                  ")
        print(" 2. Dólares a Soles                  ")
        print(" 3. Salir                            ")
        print("====================================")

        opcion = input(" Seleccione una opción: ")

        if opcion == '3':
            print(" Saliendo del sistema...")
            break
        
        elif opcion in ['1', '2']:
            try:
                monto = float(input(" Ingrese el monto: "))
                if opcion == '1':
                    resultado = realizar_conversion(monto, 1/tasa_cambio)
                    print(f"\n {monto} Soles equivalen a {resultado} Dólares.")
                else:
                    resultado = realizar_conversion(monto, tasa_cambio)
                    print(f"\n {monto} Dólares equivalen a {resultado} Soles.")
            except ValueError:
                print("\n [ERROR]: El monto debe ser un número.")
            input("\n Presione Enter para regresar al menú...")
            
        else:
            print("\n [ERROR]: Opción no válida.")
            input("\n Presione Enter para continuar...")

if __name__ == "__main__":
    ejecutar_interfaz()