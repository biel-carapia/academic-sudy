#include <stdio.h>

void calcularPrecoTotal(float precoUnitario[], int quantidade[], int numItens, float *precoTotal) {

    *precoTotal = 0;

    for (int i = 0; i < numItens; i++) {

        *precoTotal += precoUnitario[i] * quantidade[i];

    }

}

int main() {

    int numItens;

    printf(" Digite o número de itens comprados: ");

    scanf("%d", &numItens);

    float precoUnitario[numItens];

    int quantidade[numItens];

    float precoTotal;

    // Entrada dos preços unitários e quantidades de cada item

    for (int i = 0; i < numItens; i++) {

        printf("\n Digite o preço unitário do item %d: ", i + 1);

        scanf("%f", &precoUnitario[i]);

        printf(" Digite a quantidade do item %d: ", i + 1);

        scanf("%d", &quantidade[i]);

    }

    // Chamada da função para calcular o preço total

    calcularPrecoTotal(precoUnitario, quantidade, numItens, &precoTotal);

    // Exibindo o preço total da compra

    printf("\n Preço total da compra: R$ %.2f\n\n", precoTotal);

 

    return 0;

}