"""
Faça um programa que leia o destino do passageiro, se a viagem inclui retorno (ida
e volta) e informe o preço da passagem. Obs.: A tabela de valores está no PDF da atividade. # noqa: E501
"""

region = """
    1 - Região Norte
    2 - Região Nordeste
    3 - Região Centro-oeste
    4 - Região Sul
"""
ticket = """
    1 - Somente Ida
    2 - Ida e Volta
"""

print(region)
region_value = int(input("Digite o valor referente ao Destino: "))

print(ticket)
ticket_value = int(input("Agora digite o da Passagem: "))

if region_value == 1 and ticket_value == 1:
    print("Valor da passagem de Ida para Região Norte fica R$500")
elif region_value == 1 and ticket_value == 2:
    print("Valor da passagem de Ida e Volta para Região Norte fica R$900")

elif region_value == 2 and ticket_value == 1:
    print("Valor da passagem de Ida para Região Nordeste fica R$350 reais")
elif region_value == 2 and ticket_value == 2:
    print("Valor da passagem de Ida e Volta para Região Nordeste fica R$650 reais")  # noqa: E501

elif region_value == 3 and ticket_value == 1:
    print("Valor da passagem de Ida para Região Centro-oeste fica R$350 reais")
elif region_value == 3 and ticket_value == 2:
    print("Valor da passagem de Ida e Volta para Região Centro-oeste fica R$600 reais")  # noqa: E501

elif region_value == 4 and ticket_value == 1:
    print("Valor da passagem de Ida para Região Sul fica R$300 reais")
elif region_value == 4 and ticket_value == 2:
    print("Valor da passagem de Ida e Volta para Região Sul fica R$550 reais")  # noqa: E501
