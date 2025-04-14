#include <stdio.h>


int main(){

    int *ptr;
    inr valor = 10;
    
    ptr = &valor;
    
    printf("Endereço = %x", &valor);
    printf("Endereço = %s", ptr);
    printf("Valor = %d", *ptr);
    
    return 0;
    
    
    
}
    