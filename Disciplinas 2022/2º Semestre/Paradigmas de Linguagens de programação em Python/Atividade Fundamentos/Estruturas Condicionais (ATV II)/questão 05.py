"""
Segundo uma tabela médica, o peso ideal está relacionado com a altura e o sexo.
Faça um programa que receba a altura e o sexo de uma pessoa, após isso calcule
e imprima o seu peso ideal, utilizando as seguintes fórmulas:
• Para homens: (72,7 * A) – 58
• Para mulheres: (62,1 * A) – 44,7
Em que: A = Altura
"""

print("Digite 'M' para MASCULINO ou 'F' para FEMININO")
sexo = str(input("Digite seu sexo:"))
alt = float(input("Digite sua altura:"))

if sexo =='M':
    p_ideal = (72.7 * alt) - 58 
    print("Seu peso ideal é: %.2fkg" % p_ideal)

if sexo =='F':
    p_ideal = (62.1 * alt) - 44.7
    print("Seu peso ideal é: %.2fkg " %  p_ideal)    
