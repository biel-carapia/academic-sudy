#include <stdio.h>

void decimalParaBinario(int decimal){
    if(decimal > 0){
        decimalParaBinario(decimal / 2);
        printf("%d", decimal % 2);
    }
}

int main(){
    int numeroDecimal;

    printf("\nDigite um numero decimal: ");
    scanf("%d", &numeroDecimal);

    if(numeroDecimal >= 0){

        printf("O numero binario correspondente e: ");
        decimalParaBinario(numeroDecimal);
        printf("\n\n");
    }else{
        printf("Digite um numero decimal não negativo.\n");
    }



    return 0;
}

/*

#include <stdio.h>

int somar(int valor) {

    if (valor != 0) { // Critério de parada

        return valor + somar(valor - 1); // Chamada recursiva

    } else {

        return valor;

    }

}

int main() {

    int n, resultado;

    printf("\nDigite um numero inteiro positivo: ");

    scanf("%d", &n);

    resultado = somar(n); // Fazendo a primeira chamada da função

    printf("\nResultado da soma = %d", resultado);

    return 0;

}
*/