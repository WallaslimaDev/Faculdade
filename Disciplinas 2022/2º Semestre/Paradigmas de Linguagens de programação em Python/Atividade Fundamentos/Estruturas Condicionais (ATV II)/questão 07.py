"""
Escreva um programa que leia um peso na Terra e o número de um planeta e
imprima o valor correspondente do peso neste planeta. A relação de planetas é
dada a seguir juntamente com o valor das gravidades relativas à Terra. Para
calcular o peso no planeta use a fórmula: 
PP=PT/10 * 6
Em que:
PP = Peso no planeta
PT = Peso na Terra
G = Gravidade relativa

Gravidade | Planeta

0.37   | Mercúrio

0.88   |  Vênus 

0.38   | Marte

2.64   | Júpiter

1.15   | Saturno

1.17   | Urano
"""


print("Digite 1 para Mercúrio")
print("Digite 2 para Vênus")
print("Digite 3 para Marte")
print ("Digite 4 para Júpiter")
print ("Digite 5 para Saturno")
print ("Digite 6 para Urano")
pp= int(input("Escolha o planeta: "))
pt = float(input("Digite o peso na Terra:  "))


if pp == 1:
    m = (pt / 10) * 0.37
    print("O peso em Mercúrio do item informado, é: %.2f Kg " % m)
if pp == 2:
    v= (pt / 10) * 0.88
    print("O peso em Vênus do item informado, é: %.2fKg " % v)  
if pp == 3:
    marte = (pt / 10) * 0.38
    print("O peso em Marte do item informado, é: %.2fKg " % marte)
if pp == 4:
    j= (pt / 10) * 2.64
    print("O peso em Júpiter do item informado, é: %.2fKg " % j)
if pp == 5:
    s= (pt / 10) * 1.15
    print("O peso em Saturno do item informado, é: %.2fKg " % s)
if pp == 6:
    u= (pt / 10) * 1.17
    print("O peso em Urano do item informado, é: %.2fKg " % u)              


    
