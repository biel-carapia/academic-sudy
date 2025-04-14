#include <stdio.h>

int main(){

    float idade;

    printf("Digite sua idade: \n");
    scanf("%f", &idade);

    if (idade>=18){
        printf("Você já pode tirar sua carteira de Habilitação você é maior de 18");
    }

    return 0;
}