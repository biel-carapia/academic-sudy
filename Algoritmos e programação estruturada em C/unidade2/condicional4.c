#include <stdio.h>

int main(){

    char opcao;

    float valor, total;

    printf("\n Digite o valor da compra \n");
    scanf("%f", &valor);

    printf("\n Digite a letra que representa o desconto a ser aplicado:\n");
    printf("\ta - 10%% de desconto\n");
    printf("\tb - 15%% de desconto\n");
    printf("\n Digite sua opção:");

    scanf("%s", &opcao);

    switch(opcao){
        case 'a':
            total = valor - (valor*0.10);
            printf(" \nValor final da compra: R$ %.2f\n", total);
            break;
        case 'b':
            total = valor - (valor*0.20);
            printf(" \nValor final da compra: R$ %.2f\n", total);
            break;
        default:
            printf("opcao invalida\n");
    }

    return 0;

}