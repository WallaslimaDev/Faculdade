text = """
    1 - Auxiliar de Escritorio
    2 - Secretario(a)
    3 - Cozinheiro(a)
    4 - Entregador(a)
"""
print(text)
office = int(input("Digite o numero referente ao cargo: "))
salary = float(input("Digite o valor do salario: "))

if office == 1:
    salary += (salary * 0.01)
    print(f"Salario de Auxiliar de Escritorio reajustado para R${salary}")
elif office == 2:
    salary += (salary * 0.09)
    print(f"Salario de Secretario(a) reajustado para R${salary}")
elif office == 3:
    salary += (salary * 0.05)
    print(f"Salario de Cozinheiro(a) reajustado para R${salary}")
elif office == 4:
    salary += (salary * 0.12)
    print(f"Salario de Entregador(a) reajustado para R${salary}")
