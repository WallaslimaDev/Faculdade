"""
O banco Facimp concederá um crédito especial com juros de 2% aos seus clientes
de acordo com o saldo médio no último ano. Faça um programa que leia o saldo
médio de um cliente e calcule o valor do crédito de acordo com a tabela a seguir. O
programa deve imprimir uma mensagem informando o saldo médio e o valor de
crédito.

Saldo Médio | Percentual
de 0 a 500  | nenhum crédito
de 501 a 1000 | 30% do valor do saldo médio
de 1001 a 3000 | 40% do valor do saldo médio
acima de 30001 | 50% do valor do saldo médio
"""
print("Bem vindo ao Banco FACIMP :)")
saldo = float(input("Informe seu saldo médio: "))


if (saldo>0  and saldo <=500):
    print("Com o saldo médio %d, voçê não possui crédito para a operação" % saldo)
elif (saldo >= 501 and saldo<=1000):
    valor = (saldo * 0.30)
    print("Com o saldo médio %d, o seu limite de crédito é: %d" % (saldo,valor))
elif (saldo >=1001 and saldo<=3000):
    valor = (saldo * 0.4) 
    print("Com o saldo médio %d, o seu limite de crédito é: %d" % valor)
elif (saldo>3001):
    valor = (saldo * 0.5) 
    print("Com o saldo médio %d, o seu limite de crédito é %d" % valor)
            
