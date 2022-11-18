"""
Faça um programa que leia "n" valores. O programa deve inicialmente solicitar ao
usuário que informe a quantidade desejada de valores a ser informada, depois ler
os "n" valores e ao final imprimir a média aritmética dos valores lidos."""
i = 1
soma = 0
n = int(input("Digite a quantidade desejada de valores:"))
print("Quantidade informada: ",  n)

for i in range(n):
    num = int(input("Informe o numero:"))
    soma = soma+num
    media = soma / n

print(f"Média({soma}/{n}): {media} ")
