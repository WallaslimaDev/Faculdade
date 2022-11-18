////Escreva um programa que contenha duas variaveis inteiras. 
//Compare seus enderec¸os e ´exiba o maior endereço.
#include <stdio.h>
#include <stdlib.h>

int main ()
{
  int num_1;
  int num_2;
  
	printf("Digite o primero numero: ");
	scanf("%d", &num_1);
	
    printf("Digite o segundo numero: ");
	scanf("%d", &num_2);
         
    printf("\nEndereco numero 1: %x\n", &num_1);
	printf("Endereco numero 2: %x\n", &num_2);       

    if(&num_2 > &num_1)
	{
    	printf("\nNUMERO 2 TEM O MAIOR ENDERECO DE MEMORIA\n");
    }
    else
    {
		printf("\nNUMERO 1 TEM O MAIOR ENDERECO DE MEMORIA\n");
    }
    
    system("pause");
}
