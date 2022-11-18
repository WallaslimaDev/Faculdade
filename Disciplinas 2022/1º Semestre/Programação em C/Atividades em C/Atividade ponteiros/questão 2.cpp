#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>

//Escreva um programa que contenha duas variaveis inteiras. 
//Compare seus endereços e exiba o maior endereço.

int main()
{
	int valor_1 = 14;
	int valor_2 = 04;
	
	printf("Valor 1: %d\n", valor_1);
	printf("Valor 2: %d\n", valor_2);
	
	printf("\nEndereco de valor 1: %x\n", &valor_1);
	printf("Endereco de valor 2: %x\n", &valor_2);
	
	if (&valor_1 > &valor_2)
	{
		printf("\nEndereco do valor 1 e maior ");
	}
	 else
	{
		printf("\nEndreco do valor 2 e maior  ");
	}
	system("pause");
}
