#include<stdio.h>
#include <stdlib.h>

void DataAtual(int dia, int mes, int ano);

int main(void)
{
	int dia, mes, ano;
	
	printf("Digita o dia: ");
    scanf("%i",&dia);
    
    printf("Digita o mes: ");
    scanf("%i",&mes);
    
    printf("Digita o ano: ");
    scanf("%i",&ano);
    
    DataAtual(dia, mes, ano);
    
    return(0);
}

void DataAtual(int dia, int mes, int ano)
{
	const char* meses[] = 
	{
	"Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
	};
        
	printf("\nData informada por extenso: %i de %s de %i\n", dia, meses[mes - 1], ano);
}


