#include<stdio.h>
#include <stdlib.h>

int dobro(int N1)
{
	int resultado;
	resultado = N1 * 2;
	return(resultado);
}

int main(void)
{
	int V1, dobrado;

	printf("Digite um valor para achar o dobro: ");
	scanf("%d", &V1);

	dobrado = dobro(V1);

	printf("Dobro de %d= %d\n", V1, dobrado);
}


