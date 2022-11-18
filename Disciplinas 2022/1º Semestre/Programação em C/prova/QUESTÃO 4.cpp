#include<stdio.h>
#include<conio.h>

int somar_numeros(int n1,int n2); 

int main()
{
	int n1=0,n2=0,soma=0; 

	printf("Digite o primeiro numero:"); 
	scanf("%d",&n1); 

	printf("Digite o segundo numero:"); 
	scanf("%d",&n2); 

	soma = somar_numeros(n1,n2); 

	printf("A soma dos numeros entre %d e %d = %d",n1,n2,soma); 
getch(); 
}

int somar_numeros(int n1,int n2) 
{ 
	int i,s=0; 
	
		for(i = n1 + 1;i <= n2 - 1;i++) s = s + i; 
		
	return(s);
}
