"""Faça um programa que permita entrar com números e
imprimir o quadrado de cada número digitado
até entrar um número múltiplo de 6 que deverá ter seu quadrado
impresso também."""

while 1:
    num = int(input("Digite um numero ou multiplo de 6 para encerrar:"))
    quadrado = num**2
    print(f"Quadrado do numero informado:{quadrado} ")
    if (num % 6) != 0:
        continue
    else:
        break
