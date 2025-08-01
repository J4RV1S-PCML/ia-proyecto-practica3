import sys
import os
import math

class CalculadoraUnidades:
    @staticmethod
    def metros_a_centimetros(metros):
        """
        Convierte metros a centímetros.
        Maneja errores si el valor no es numérico.
        """
        try:
            return float(metros) * 100
        except (ValueError, TypeError):
            print("Error: El valor ingresado no es numérico.")
            return None
    
    @staticmethod
    def millas_a_kilometros(millas):
        """
        Convierte millas a kilómetros.
        Maneja errores si el valor no es numérico.3
        """
        try:
            return float(millas) * 1.60934
        except (ValueError, TypeError):
            print("Error: El valor ingresado no es numérico.")
            return None
    
    @staticmethod
    def centimetros_a_metros(centimetros):
        """
        Convierte centímetros a metros.
        Maneja errores si el valor no es numérico.
        """
        try:
            return float(centimetros) / 100
        except (ValueError, TypeError):
            print("Error: El valor ingresado no es numérico.")
            return None
    
    @staticmethod
    def metros_a_milimetros(metros):
        """
        Convierte metros a milímetros.
        Maneja errores si el valor no es numérico.
        """
        try:
            return float(metros) * 1000
        except (ValueError, TypeError):
            print("Error: El valor ingresado no es numérico.")
            return None
    
    @staticmethod
    def milimetros_a_metros(milimetros):
        """
        Convierte milímetros a metros.
        Maneja errores si el valor no es numérico.
        """
        try:
            return float(milimetros) / 1000
        except (ValueError, TypeError):
            print("Error: El valor ingresado no es numérico.")
            return None
    
    @staticmethod
    def metros_a_kilometros(metros):
        """
        Convierte metros a kilómetros.
        Maneja errores si el valor no es numérico.
        """
        try:
            return float(metros) / 1000000
        except (ValueError, TypeError):
            print("Error: El valor ingresado no es numérico.")
            return None
    
    @staticmethod
    def kilometros_a_metros(kilometros):
        """
        Convierte kilómetros a metros.
        Maneja errores si el valor no es numérico.
        """
        try:
            return float(kilometros) * 1000000
        except (ValueError, TypeError):
            print("Error: El valor ingresado no es numérico.")
            return None

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
    return input("Elija una opción: ")

def main():
    calc = CalculadoraUnidades()
    
    while True:
        try:
            opcion = mostrar_menu()
            
            if opcion == "0":
                print("Saliendo del programa...")
                break
                
            if opcion not in ["1", "2", "3", "4", "5", "6"]:
                print("Opción inválida. Intente nuevamente.")
                continue
                
            conversiones = {
                "1": (calc.metros_a_centimetros, "metros", "centímetros"),
                "2": (calc.centimetros_a_metros, "centímetros", "metros"),
                "3": (calc.metros_a_milimetros, "metros", "milímetros"),
                "4": (calc.milimetros_a_metros, "milímetros", "metros"),
                "5": (calc.metros_a_kilometros, "metros", "kilómetros"),
                "6": (calc.kilometros_a_metros, "kilómetros", "metros")
            }
            
            funcion, unidad_entrada, unidad_salida = conversiones[opcion]
            valor = float(input(f"Ingrese la medida en {unidad_entrada}: "))
            resultado = funcion(valor)
            print(f"{valor} {unidad_entrada} equivalen a {resultado} {unidad_salida}.")
            
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            break

if __name__ == "__main__":
    main()