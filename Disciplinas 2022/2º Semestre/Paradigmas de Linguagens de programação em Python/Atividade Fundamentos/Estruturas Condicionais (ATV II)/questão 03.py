"""
Faça um programa que receba um número inteiro e verifique se este número é
maior que 20, em caso afirmativo o programa deverá multiplicar o valor por 2 e em
caso negativo deve multiplicar por 4. Após realizar o cálculo o programa deve
imprimir a mensagem: Resultado: <valor do resultado>, em que <valor do
resultado> deve ser substituído pelo resultado do cálculo.
"""

n1 = int(input("Digite um numero:"))

if n1>20:
    maior = n1 * 2
    print("%d x 2" % n1) 
    print("Resultado: ", maior)

if n1<20:
    menor = n1 * 4
    print("%d X 4" % n1) 
    print("Resultado: ", menor)    




