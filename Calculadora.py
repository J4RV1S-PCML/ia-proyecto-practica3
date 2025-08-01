# Calculadora de medidas - v0.1
# Autor: [Tu Nombre]         
# Fecha: [Fecha de Creación]
# Descripción: Este script implementa una calculadora simple para convertir medidas entre diferentes unidades.   
# Importando bibliotecas necesarias
# Feat: agrega km_a_millas()
# Función para convertir kilómetros a millas

# Función para convertir millas a kilómetros 
import sys  
import os   
import math

# Función para convertir metros a centímetros
def metros_a_centimetros(metros):
    return metros * 100

def millas_a_kilometros(millas):
    return millas * 1.60934

# Función para convertir centímetros a metros
def centimetros_a_metros(centimetros):
    return centimetros / 100

# Función para convertir metros a milímetros
def metros_a_milimetros(metros):
    return metros * 1000

# Función para convertir milímetros a metros
def milimetros_a_metros(milimetros):
    return milimetros / 1000

# Función para convertir metros a kilómetros
def metros_a_kilometros(metros):
    return metros / 1000000

# Función para convertir kilómetros a metros
def kilometros_a_metros(kilometros):
    return kilometros * 1000000    

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\nCalculadora de Medidas")
    print("1. Convertir metros a centímetros")
    print("2. Convertir centímetros a metros")
    print("3. Convertir metros a milímetros")
    print("4. Convertir milímetros a metros")
    print("5. Convertir metros a kilómetros")
    print("6. Convertir kilómetros a metros")
    print("0. Salir")    
    print()
    opcion = input("Elija una opción: ")
    return opcion

# Función principal
def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            metros = float(input("Ingrese la medida en metros: "))
            centimetros = metros_a_centimetros(metros)
            print(f"{metros} metros equivalen a {centimetros} centímetros.")
        elif opcion == "2":
            centimetros = float(input("Ingrese la medida en centímetros: "))
            metros = centimetros_a_metros(centimetros)
            print(f"{centimetros} centímetros equivalen a {metros} metros.")
        elif opcion == "3":
            metros = float(input("Ingrese la medida en metros: "))
            milimetros = metros_a_milimetros(metros)
            print(f"{metros} metros equivalen a {milimetros} milímetros.")
        elif opcion == "4":
            milimetros = float(input("Ingrese la medida en milímetros: "))
            metros = milimetros_a_metros(milimetros)
            print(f"{milimetros} milímetros equivalen a {metros} metros.")
        elif opcion == "5":
            metros = float(input("Ingrese la medida en metros: "))
            kilometros = metros_a_kilometros(metros)
            print(f"{metros} metros equivalen a {kilometros} kilómetros.")
        elif opcion == "6":
            kilometros = float(input("Ingrese la medida en kilómetros: "))
            metros = kilometros_a_metros(kilometros)
            print(f"{kilometros} kilómetros equivalen a {metros} metros.")
        elif opcion == "0":
            print("Saliendo del programa.")
            sys.exit()
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()