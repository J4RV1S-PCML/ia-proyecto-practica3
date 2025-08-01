# Calculadora de medidas – v0.1
# Autor: [Seu Nome]         
# Data: [Data de Criação]
# Descrição: Este script implementa uma calculadora simples para converter medidas entre diferentes unidades.   
# Importando bibliotecas necessárias
# Feat: agrega km_a_millas()
# Função para converter quilômetros para milhas

# Função para converter milhas para quilômetros 
import sys  
import os   
import math
# Função para converter metros para centímetros
def metros_para_centimetros(metros):
    return metros * 100
def milhas_para_quilometros(milhas):
    return milhas * 1.60934
# Função para converter centímetros para metros
def centimetros_para_metros(centimetros):
    return centimetros / 100
# Função para converter metros para milímetros
def metros_para_milimetros(metros):
    return metros * 1000
# Função para converter milímetros para metros
def milimetros_para_metros(milimetros):
    return milimetros / 1000
# Função para converter metros para quilômetros
def metros_para_quilometros(metros):
    return metros / 1000000
# Função para converter quilômetros para metros
def quilometros_para_metros(quilometros):
    return quilometros * 1000000    
# Função para exibir o menu de opções
def exibir_menu():
    print("\nCalculadora de Medidas")
    print("1. Converter metros para centímetros")
    print("2. Converter centímetros para metros")
    print("3. Converter metros para milímetros")
    print("4. Converter milímetros para metros")
    print("5. Converter metros para quilômetros")
    print("6. Converter quilômetros para metros")
    print("0. Sair")    
    print()
    opcao = input("Escolha uma opção: ")
    return opcao
# Função principal
def main():
    while True:
        opcao = exibir_menu()
        if opcao == "1":
            metros = float(input("Digite a medida em metros: "))
            centimetros = metros_para_centimetros(metros)
            print(f"{metros} metros equivalem a {centimetros} centímetros.")
        elif opcao == "2":
            centimetros = float(input("Digite a medida em centímetros: "))
            metros = centimetros_para_metros(centimetros)
            print(f"{centimetros} centímetros equivalem a {metros} metros.")
        elif opcao == "3":
            metros = float(input("Digite a medida em metros: "))
            milimetros = metros_para_milimetros(metros)
            print(f"{metros} metros equivalem a {milimetros} milímetros.")
        elif opcao == "4":
            milimetros = float(input("Digite a medida em milímetros: "))
            metros = milimetros_para_metros(milimetros)
            print(f"{milimetros} milímetros equivalem a {metros} metros.")
        elif opcao == "5":
            metros = float(input("Digite a medida em metros: "))
            quilometros = metros_para_quilometros(metros)
            print(f"{metros} metros equivalem a {quilometros} quilômetros.")
        elif opcao == "6":
            quilometros = float(input("Digite a medida em quilômetros: "))
            metros = quilometros_para_metros(quilometros)
            print(f"{quilometros} quilômetros equivalem a {metros} metros.")
        elif opcao == "0":
            print("Saindo do programa.")
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()      