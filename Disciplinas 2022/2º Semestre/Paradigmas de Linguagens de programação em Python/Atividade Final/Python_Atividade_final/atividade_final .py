text = """        
----------------------LISTA DE EXERCÍCIOS----------------------
             LISTA 1: FUNDAMENTOS DO PYTHON
1.Faça um Programa que mostre a mensagem Alo mundo na tela. 
2.Faça um Programa que peça dois números e imprima a soma
             LISTA 2: ESTRUTURAS CONDICIONAIS
1.Faça um programa que receba um número inteiro e verifique se este número émaior que 20,em caso afirmativo o programa deverá imprimir a mensagem:Maiorque 20.
2.Faça um programa que receba um número inteiro e verifique se este número émaior que 20, em caso afirmativo o programa deverá multiplicar o valor por 2 e 
após o cálculo imprimir a mensagem: (Resultado: <valor do resultado>),em que<valor do resultado> deve ser substituído pelo resultado do cálculo.
             LISTA 3: ESTRUTURA DE REPETIÇÃO
1.Faça um programa que realize a soma de todos os valores inteiros de 1 a n, sendo que n deve ser informado pelo usuário
2.Faça um programa que permita entrar com números e imprimir o quadrado de cadanúmero digitado até entrar um número múltiplo de 6 que deverá ter seu quadradoimpresso também
"""
import os 
"""Função para limpar o terminal"""
os.system('cls' if os.name == 'nt' else 'clear')

#Exercício 1 - Fundamentos do Python
def fundamentos_py_1 (): #definição da função
    return "Alo, mundo" #retorno da função
#Exercício 2 - Fudamentos do Python    
def fundamentos_py_2(n1,n2):  #definição da função    
    soma= n1 + n2 #calculo da função
    return soma #retorno da função

#Exercício 1 - Estruturas Condicionais
def estrutura_condicional_1(n1): #definição da função
    if (n1>20): 
        return "Maior que 20" #retorno da função
    else:
        return f"Numero digitado:{n1}" #retorno da função

#Exercício 2 - Estruturas Condicionais        
def estrutura_condicional_2(number): #definição da função
    if (number>20): #calculo da função
        number *= 2
    return f"Resultado: {number}" #retorno da função

#Exercício 1 - Estruturas de Repetição
def estrutura_repeticao_1(value): #definição da função 
    return result / 10 #retorno da função

#Exercício 2- Estruturas de Repetição
def estrutura_repeticao_2(num): #definição da função 
    quadrado = num**2 #calculo da função
    return quadrado #retorno da função

while 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    print (text)
    """Programa solicita ao usuário a informação de qual lista ele deseja executar"""
    list = int(input("-Selecione uma lista(1,2 ou 3), ou digite 0 para finalizar:"))
    if list == 0:
        """Se digitar 0(deseja encerrar), o programa solitica a confirmação da ação"""
        n=int(input("Deseja realmente encerrar? Digite 1 pra SIM:"))
        if n ==1:
            """Executa o fim do código"""
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Programa Encerrado!")
            break
    elif list == 1:
        """Escolhida a lista 1, o programa irá perguntar qual exercício o usuário deseja executar"""
        exercicio = int(input("Escolha um exercício(1 ou 2): "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if exercicio== 1:
            """Invocando a funcao e retornado para a variavel"""
            n = fundamentos_py_1()
            """Imprimindo a variavel que recebeu o resultado"""
            print (n)
            continue

        elif exercicio == 2:
            """Executa o que se pede no Exercício 2"""
            n1 = int(input("Digite um numero:"))
            n2 = int(input("Digite outro numero:"))
            """Invocando a funcao e retornado para a variavel"""
            soma = fundamentos_py_2(n1,n2)
            """Imprimindo a variavel que recebeu o resultado"""
            print(f"Soma:{soma}")
            continue    
    elif list == 2:
        """Escolhida a lista 2, o programa irá perguntar qual exercício o usuário deseja executar"""
        exercicio = int(input("Escolha um exercício(1 ou 2): "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if exercicio== 1:
            """Executa o que se pede no Exercício 1"""
            n1 = int(input("Digite um numero:"))
            """Invocando a funcao e retornado para a variavel"""
            n = estrutura_condicional_1 (n1)
            """Imprimindo a variavel que recebeu o resultado"""
            print (f"{n}")
            continue

        elif exercicio == 2:
            """Executa o que se pede no Exercício 2"""
            number = int(input("Digite um numero:"))
            """Invocando a funcao e retornado para a variavel"""
            n = estrutura_condicional_2(number)
            """Imprimindo a variavel que recebeu o resultado"""
            print(f"{n}")
            continue

    elif list == 3:
        """Escolhida a lista 3, o programa irá perguntar qual exercício o usuário deseja executar"""
        exercicio = int(input("Escolha um exercício(1 ou 2): "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if exercicio== 1:
            """Executa o que se pede no Exercício 1"""
            count = 0
            result: float = 0
            while count < 10:
                value = float(input("Digite um numero: "))
                result += value
                count += 1
            """Invocando a funcao e retornado para a variavel"""    
            media = estrutura_repeticao_1(value)
            """Imprimindo a variavel que recebeu o resultado"""
            print (f"{media}") 
            continue   
        elif exercicio == 2:
            """Executa o que se pede no Exercício 2"""
            while 1:
                num = int(input("Digite um numero ou multiplo de 6 para encerrar:"))
                """Invocando a funcao e retornado para a variavel"""
                n= estrutura_repeticao_2(num)
                """Imprimindo a variavel que recebeu o resultado"""
                print (f"Quadrado do numero informado:{n}") 
                if (num % 6) != 0:
                    continue
                else:
                    break
                
            continue
        else:
            """Caso o usuário insira uma opção não disponível no menu"""
            print("Opção Inválida")
            continue    
    else:
        """Caso o usuário insira uma opção não disponível no menu"""
        print("A Opção digitada é Inválida!")
        continue    