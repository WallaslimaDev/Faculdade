"""
Faça um programa que realize a soma de todos os valores inteiros de 1 a n,
sendo que n deve ser informado pelo usuário."""
soma = 0
i = 1
n = int(input("Informe o numero n:"))

while i <= n:
    soma += i
    i += 1
print(f"Soma:{soma} ")
