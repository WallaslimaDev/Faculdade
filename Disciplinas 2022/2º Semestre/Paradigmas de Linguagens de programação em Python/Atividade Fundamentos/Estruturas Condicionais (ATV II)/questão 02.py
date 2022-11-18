"""
Faça um programa que receba um número inteiro e verifique se este número é
maior que 20, em caso afirmativo o programa deverá multiplicar o valor por 2 e
após o cálculo imprimir a mensagem: "Resultado: <valor do resultado>", em que
<valor do resultado> deve ser substituído pelo resultado do cálculo.
"""

number = int(input("Digite um número: "))

if number > 20:
    number *= 2
    print(f"Resultado: {number}")
else: 
    print(f"Numero digitado: {number}")