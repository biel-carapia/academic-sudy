#include <stdio.h>
#include <stdlib.h>


int main(){

    int *vet = NULL;
    int tam = 0;

    vet = (int *) malloc(5 * sizeof(int));

    if(vet == NULL){
        printf("Falha na alocação de memória\n");
        return 1; // Encerra o programa com código de erro
    }

    printf("Vetor inicialmente alocado com sucesso.\n");

    for(int i = 0; i < 3; i++){
        vet[tam] = i * 2;
        tam++;
    }

    printf("Elementos do vetor: \n");
    for(int i = 0; i < tam; i++){
        printf("%d", vet[i]);
    }
    printf("\n");

    // Realocar o array para acomodar mais elementos
    int novotamanho = 10;
    vet = (int *)realloc(vet, novotamanho * sizeof(int));

    if(vet == NULL){
        printf("Falha na realocação de memória.\n ");
        return 1; // Rncerrar o programa com código de erro
    }

    printf("Vetor realocado com sucesso.\n");

    for(int i = 3; i < novotamanho; i++){
        vet[tam] = i * 2;
        tam++;
    }

    printf("Elementos do array após realocação:\n");
    for(int i = 0; i < tam; i++){
        printf("%d", vet[i]);
    }
    printf("\n");

    // Liberar a memória alocada
    free(vet);


}