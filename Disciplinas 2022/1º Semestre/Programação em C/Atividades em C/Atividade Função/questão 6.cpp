#include <stdio.h>
#include <stdlib.h>

//converter hora para segundo:
// 'hora' x 60 x 60= 'segundo'.

//converter minuto para segundo:
// 'minuto' x 60 = 'segundo'.


 float segundos(float H, float M, float S) 
{
		float min,calculo, ho;
		calculo=(S+(H*60*60)+(M*60));
		return calculo;
}

int main () 
{
	float H,M, S;
	 
	
	printf("\tCONVERSAO DE HORAS EM SEGUNDOS");
	printf("\n\nDigite a hora: ");
	scanf("%f",&H);
	
	printf("Digite o Minuto: ");
	scanf("%f", &M);
	
	printf("Digite o segundo: ");
	scanf("%f", &S);
	
	printf("\nApos convertido: %f segundos",segundos(H,M,S));
	
	
}
