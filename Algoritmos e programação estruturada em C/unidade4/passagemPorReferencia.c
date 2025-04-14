#include <stdio.h>

// int valor = 5;


void dobrar(int *numero){
    *numero *= 2;
}

// void dobrar(){
//    valor *= 2;
// }


int main(){
    int valor = 5;

    printf("Valor antes da chamada da função: %d\n", valor);

    dobrar(&valor);

    printf("Valor antes da chamada da função: %d\n", valor);


    return 0;
}

/*
#include <stdio.h>

struct Pessoa {

    char nome[50];

    int idade;

};

void modificarPessoa(struct Pessoa *p) {

    p->idade = 30;

}

 

int main() {

    struct Pessoa pessoa1;

    strcpy(pessoa1.nome, "João");

    pessoa1.idade = 25;

 

    modificarPessoa(&pessoa1);

 

    printf("Nome: %s\n", pessoa1.nome);

    printf("Idade: %d\n", pessoa1.idade);

 

    return 0;

}
    
*/