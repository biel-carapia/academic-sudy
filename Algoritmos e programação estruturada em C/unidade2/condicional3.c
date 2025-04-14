#include <stdio.h>

int main(){

    int num = 10;

    if(num < 100){
        printf("Menor que 100");
    }else if(num < 1000){
        printf("Menor que 1000");
    }else if(num < 10000){
        printf("Menor que 10000");
    }else{
        printf("Maior ou igual a 10000");
    }

    return 0;

}