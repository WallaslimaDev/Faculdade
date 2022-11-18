#include<stdio.h>

void alteraValor(int a, int b);
 
int main(void)
{
    int N1, N2,a, b;
    printf("Digite o primeiro valor(A):  ");
    scanf("%d", &a);
    
    printf("Digite o segundo valor(B):  ");
    scanf("%d", &b);
    
    printf("Valor A: %d ", a);
    printf("\nValor B: %d ", b);
    
	alteraValor(a,b);
	return 0;
}

	void alteraValor(int num1, int num2)
{
	int aux, a, b;
    aux = num1;
    a = num2;
    b = aux;
	
	printf("\n\nVALORES INVERTIDOS\n");
    
    printf("\nValor A: %d ",a );
    printf("\nValor B: %d ",b );
    
    printf("\n\nENDERECOS\n");
    printf("\nEndereco valor A: %x\n", &a);
    printf("Endereco valor B: %x ", &b);
}


