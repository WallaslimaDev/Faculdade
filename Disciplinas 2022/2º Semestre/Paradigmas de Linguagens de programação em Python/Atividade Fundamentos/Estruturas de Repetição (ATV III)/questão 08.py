# cSpell: disable
"""
Faça um programa que leia 10 números positivos e imprima o quadrado de cada
número. Para cada entrada de dados deverá haver um trecho de validação para
que um número negativo não seja aceito pelo programa.
"""
count = 0
while count < 10:
    number = int(input("Digite um número: "))
    if number % 2 == 0:
        print(f"Valor digitato elevado ao quadrado: {number ** 2}")
    else:
        print("Digite apenas numeros positivos!")

    count += 1
