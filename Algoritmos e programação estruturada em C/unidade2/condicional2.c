#include <stdio.h>

int main(){

    int num;
    
    printf ("Digite um número: ");
    scanf ("%d",&num);

    if (num>0) {
        printf ("\n\nO número e positivo\n");
    }else {
        printf ("O número e negativo");
    }

    return 0;
}