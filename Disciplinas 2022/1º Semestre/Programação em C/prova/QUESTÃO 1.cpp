#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <locale.h>

 typedef struct 
 {
    char nome[50];
    char endereco[50];
    int telefone;
 
	}pessoa;

int main (void)
{
    
     pessoa p[5];
     int i, x;
     char aux[50], aux2[50];
     int aux3;
    
    for(i=0; i<5; i++)
	{
    printf("\nDigite o Nome da pessoa %d :",i+1);
    fflush(stdin);
    fgets(p[i].nome, 50, stdin);
    
    printf("Digite o Endereco:");
    fgets(p[i].endereco, 50, stdin);
    
    printf("Digite o Telefone:");
    scanf("%d", &p[i].telefone);
    }
    
    for(i=0;i<4;i++){
        for (int j=i+1; j < 5; j++)
        {
            x = strcmp(p[i].nome, p[j].nome);
            if(x>0){
                strcpy(aux, p[i].nome);
                strcpy(p[i].nome, p[j].nome);
                strcpy(p[j].nome,aux);
          
                strcpy(aux2, p[i].endereco);
                strcpy(p[i].endereco, p[j].endereco);
                strcpy(p[j].endereco, aux2);
          
                aux3 = p[i].telefone;
                p[i].telefone = p[j].telefone;
                p[j].telefone = aux3;
            }
        }
    }
   
printf("\n-----LISTA DAS PESSOAS EM ORDEM ALFABETICA------");
for(i=0; i<5; i++)
{
    printf("\n\nNome: %s", p[i].nome);
    printf("Endereco: %s", p[i].endereco);
    printf("Telefone: %d\n", p[i].telefone);
}    
system ("pause");
    return 0;    
}
