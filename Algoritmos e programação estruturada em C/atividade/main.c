#include <stdio.h>

main int(){

    /******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{
    int valor1, valor2, valor3;

    int soma, subtracao, divisao, multiplicacao, validacao;
    
    char validacao2;
    
    

    printf("\nDigite o primeiro número: ");
    scanf("%d", &valor1);

    printf("\nDigite o segundo número: ");
    scanf("%d", &valor2);

    printf("\nDigite o terceiro número: ");
    scanf("%d", &valor3);
    
    validacao = valor1 > 0 && valor2 % 2 == 0;

    printf("\nO primeiro número é positivo e o segundo número é par se SIM validação é igual a 1, caso NÃO validação é igual a 0 - VALIDAÇÃO = %d", validacao == 1);
    
    printf("\nO primeiro número é maior que o segundo número: %d", valor1 > valor2);

    printf("\nO segundo número é menor que o terceiro número: %d", valor2 < valor3);

    soma = valor1 + valor2 + valor3;

    printf("\nValor da soma: %d", soma);

    subtracao = valor1 - valor2;

    printf("\nValor da subtração do primeiro número pelo segundo número: %d", subtracao);

    subtracao = valor2 - valor3;
    
    printf("\nValor da subtração do segundo número pelo terceiro número: %d", subtracao);
    
    divisao = valor1 / valor2;

    printf("\nValor da divisao do primeiro número pelo segundo número: %d", divisao);
    
    divisao = valor2 / valor3;
    
    printf("\nValor da divisao do segundo número pelo terceiro número: %d", divisao);

    multiplicacao = valor1 * valor2;

    printf("\nValor da muultiplicação do primeiro número pelo segundo número: %d", multiplicacao);
    
    multiplicacao = valor2 * valor3;
    
    printf("\nValor da muultiplicação do segundo número pelo terceiro número: %d", multiplicacao);
    
    multiplicacao = valor1 * (valor2 * valor3);
    
    printf("\nValor da multiplicacao dos três números: %d", multiplicacao);


    return 0;
}
}