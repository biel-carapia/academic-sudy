#include <stdio.h>

int fatorial(int n){
    int res = 1;
    if(n == 0){
        return 1;
    }else{
        for(int i = n; i >= 1; i--){
            res = res * i;
        }
    }

    /*
    if(n > 0){
     for(int i = n; i >= 1; i--){
            res = res * i;
        }
    }
    */

    return res;
}



int main(){


    int numero;

    printf("Digite um número inteiro positivo: ");
    scanf("%d", &numeor);

    if(numero < 0)
        printf("Numero negativo!");
    else
        printf("Resultado = %d", fatorial(numero));


    return 0;
}