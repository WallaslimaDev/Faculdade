#include <stdio.h>

    int adicao(int a, int b)
{
    int resultado;
    resultado = a + b;
}
    int subtracao(int n1, int n2)
{
    int resultado;
    resultado = n1 - n2;
    return resultado;
}
    int divisao(int n1, int n2)
{
    int resultado;
    resultado = n1 / n2;
    return resultado;
}
    int multiplicacao(int n1, int n2)
{
    int resultado;
    resultado = n1 * n2;
    return resultado;
}

int main(void)
{

    int n1,n2,resultado,op;

    printf("Digite um valor: ");
    scanf("%d",&n1);

    printf("Digite um valor: ");
    scanf("%d",&n2);

    printf("\n\n[1]Somar            [3]Subtrair");
    printf("\n[2]Multiplicar      [4]Dividir");
    printf("\n\nDigite o numero correspondente a operacao desejada: ");
    scanf("%d",&op);

    if(op == 1)
    {
        resultado = adicao(n1,n2);
        printf("\nResultado da adicao de %d + %d = %d",n1,n2,resultado);
    }

    if(op == 2)
    {
        resultado = multiplicacao(n1,n2);
        printf("\nResultado da multiplicacao de %d x %d = %d",n1,n2,resultado);
    }

    if(op == 3)
    {
        resultado = subtracao(n1,n2);
        printf("\nResultado da subtracao de %d - %d = %d",n1,n2,resultado);
    }

    if(op == 4)
    {
        resultado = divisao(n1,n2);
        printf("\nResultado da divisao de %d / %d = %d",n1,n2,resultado);
    }

    return 0;
}
