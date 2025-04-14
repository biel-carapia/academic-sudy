#include <stdio.h>

#include <stdlib.h>

int* gerarRandomico(){
    static int r[10];
    int a;

    for(a = 0; a < 10; ++a) {
        r[a] = rand() % 100; // “% 100” é usado para para limitar o rand a úmeros entre 0 e 99
        printf(“r[%d] = %d\n”, a, r[a]);
    }

    return r;
}

int main(){

    int *p;
    int I;

    p = gerarRandomico();

    for (i = 0; i < 10; i++) {
        printf("\np[%d] = %s", i, *(p + i));
    }

    return 0;

}