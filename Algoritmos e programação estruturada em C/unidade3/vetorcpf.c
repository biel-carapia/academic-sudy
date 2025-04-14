#include <stdio.h>

int main(){

    char cpf1[15]; // Vetor CPF formatado com pontos e traço
    char cpf2[11] = ""; // Vetor CPF sem formatação, inicializado como vazio
    int i = 0, n = 0;

    printf("Digite seu CPF na forma NNN.NNN.NNN-NN: \n");
    scanf("%s", cpf1);

    // Laço para percorrer todo o vetor cpf1

    // Remover pontos e traços e armazenar apenas os dígitos

    for (i = 0; i < 14; i++) {
        if (cpf1[i] == '.' || cpf1[i] == '-') {
            continue; // Ignora pontos e traços
        } else {
            // Armazena apenas os dígitos em cpf2
            cpf2[n] = cpf1[i];
            n++; // controla o tamanho do cpf2
        }
    }
    // Imprime o CPF formatado sem pontos e traços

    printf("\n\nCPF formatado = %s", cpf2);

    return 0;

}