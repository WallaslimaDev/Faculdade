# cSpell: disable
"""
Faça um programa que leia 10 valores e ao final imprima a média aritmética dos
valores lidos.
"""

count = 0
result: float = 0
while count < 10:
    value = float(input("Digite um numero: "))
    result += value
    count += 1

print(result / 10)
