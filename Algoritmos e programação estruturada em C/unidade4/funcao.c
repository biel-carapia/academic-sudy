#include <stdio.h>

void exibirMenu();
void realizarAcao(int escolha);


int main(){
    int escolha;

    do{
        exibirMenu();
        scanf("%d", &escolha);

        realizarAcao(escolha)
    }while(escolha != 0);

    return 0;
}


void exibirMenu(){
    printf("\n===== Menu =====\n");
    printf("1. Realizar Tarefa 1\n");
    printf("2. Realizar Tarefa 2\n");
    printf("3. Realizar Tarefa 3\n");
    printf("0. Sair\n");
    printf("Escolha uma opcao: ");
}

void realizarAcao(int escolha){
    switch (escolha){
        case 1:
            printf("Realizando Tarefa 1.\n\n");
            break;
        case 2:
            printf("Realizando Tarefa 2.\n\n");
            break;
        case 3:
            printf("Realizando Tarefa 3.\n\n");
            break;
        case 0:
            printf("Saindo do programa. Adeus!\n\n");
            break;
        default:
            printf("Opcao inválida. Tente novamente.\n\n");
    }
}
