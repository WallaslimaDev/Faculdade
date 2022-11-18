////Escreva um programa que declare um inteiro, um real e um char, e ponteiros para inteiro, real, e char. 
//Associe as variaveis aos ponteiros (use &). 
//Modifique os valores decada variavel usando os ponteiros. Imprima os valores das variaveis antes e apos a modificacao
#include<stdio.h>
#include <stdlib.h>

int main()
{
	int num = 14;
	float valor = 14.04;
	char letra = 'w';
	
	int *Int = &num;
	float *Float = &valor;
	char *Char = &letra;
	
	printf("\tVALORES E ENDERECOS\n");
	
	printf("\nValor variavel inteiro: %d\n", num);
	printf("Endereco inteiro: %x\n", &num);
	
	printf("\nValor variavel float: %f\n", valor);
	printf("Endereco float: %x\n", &valor);
	
	printf("\nValor variavel char: %c\n", letra);
	printf("Endereco char: %x\n\n", &letra);
	
	printf("\t VALORES DAS VARIAVEIS ANTES DAS MODIFICACOES\n");
	
	printf("\nValor variavel inteiro: %d\n", num);
	printf("Valor variavel float: %f\n", valor);
	printf("Valor variavel char: %c\n\n", letra);

	printf("\t VALORES DAS VARIAVEIS APOS MODIFICACOES \n");
	
	*Int = 2001;
	*Float = 4.14;
	*Char = 'a';
	
	printf("\nVariavel Inteiro alterada para o valor: %d\n", *Int);
	printf("Variavel float lterada para o valor: %f\n", *Float);
	printf("Variavel char alterada para o caractere: %c\n", *Char);
	
	return(0);
}