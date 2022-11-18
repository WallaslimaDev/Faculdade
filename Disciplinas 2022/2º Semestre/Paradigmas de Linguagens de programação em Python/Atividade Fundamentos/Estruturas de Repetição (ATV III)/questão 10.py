# cSpell: disable
"""
Uma transportadora utiliza caminhões que suportam até 10 toneladas de peso, as
caixas transportadas tem tamanho fixo e o caminhão comporta no máximo 200
volumes, assim, esta transportadora precisa controlar a quantidade e o peso dos
volumes para acomodar nos caminhões. Faça um programa que leia n caixas e
seu peso, ao final, o programa deve imprimir a quantidade de volumes,
o peso total dos volumes e o peso médio dos volumes.
"""
qtd_volumes = 0
peso_total = 0
peso_medio = 0
caixa = int(input("Deseja cadastrar uma caixa? 1-SIM / 2-NAO: "))

if caixa == 2:
    print("Nenhuma caixa cadastrada")
while caixa == 1:
    qtd_volumes += 1
    peso = float(input("Informe o peso da caixa:"))
    peso_total += peso
    caixa = int(input("Deseja cadastrar outra caixa? 1-SIM / 2-NAO \n"))
    peso_medio = peso_total / qtd_volumes

print(f"Quantidade de volumes:{qtd_volumes} ")
print(f"Peso total dos volumes:{peso_total} ")
print(f"Peso medio dos volumes:{peso_medio} ")
