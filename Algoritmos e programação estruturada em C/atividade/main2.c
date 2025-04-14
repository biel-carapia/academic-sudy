#include <stdio.h>


int main(){
    int n;
    int valor = 0, contador;
  
    while(n != 0){
        printf("Digite um número: ");
        scanf("%d", &n);
        n += valor;
        valor = n;
        contador = contador + 1;
    }
    
    printf("O resultado da soma é igual a: %d", valor);
    
}

/*
Cenário: Imagine que você está desenvolvendo uma ferramenta simples de cálculo, onde o
usuário deseja somar uma série de números inteiros até decidir que não deseja inserir mais
nenhum número. A cada inserção, o programa deve somar os números já inseridos e permitir
que o usuário continue até digitar o número 0 (zero), que encerra o programa e exibe o
resultado final da soma.


    printf("Valor: %d \n", valor);
  printf("n: %d \n", n);
        printf("%d", valor);

*/