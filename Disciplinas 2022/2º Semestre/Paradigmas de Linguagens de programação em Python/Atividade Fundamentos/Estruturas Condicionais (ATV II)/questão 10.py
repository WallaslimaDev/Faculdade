"""
Faça um programa que leia dois valores inteiros e efetue a adição. Caso o valor
somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8,
caso o valor somado seja menor ou igual a 20,
este deverá ser apresentado subtraindo-se 5.
"""

value1 = int(input("Digite um numero: "))
value2 = int(input("Digite um outro numero: "))

sum = value1 + value2

if sum > 20:
    sum += 8
    print(f"Resultado: {sum}")
elif sum <= 20:
    sum -= 5
    print(f"Resultado: {sum}")
