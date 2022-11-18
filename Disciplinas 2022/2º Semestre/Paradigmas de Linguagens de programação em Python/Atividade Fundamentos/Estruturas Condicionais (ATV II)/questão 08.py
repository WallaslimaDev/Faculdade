"""
Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
correspondente. Caso o usuário digite um número fora desse intervalo, deverá
aparecer uma mensagem informando que não existe mês com este número.
"""

number = int(input("Digite um valor referente ao mês desejado: "))

if number == 1:
    print("Mês de Janeiro")

if number == 2:
    print("Mês de Fevereiro")

if number == 3:
    print("Mês de Março")

if number == 4:
    print("Mês de Abril")

if number == 5:
    print("Mês de Maio")

if number == 6:
    print("Mês de Junho")

if number == 7:
    print("Mês de Julho")

if number == 8:
    print("Mês de Agosto")

if number == 9:
    print("Mês de Setembro")

if number == 10:
    print("Mês de Outubro")

if number == 11:
    print("Mês de Novembro")

if number == 12:
    print("Mês de Dezembro")
else:
    print("Não existe mês com este número")
