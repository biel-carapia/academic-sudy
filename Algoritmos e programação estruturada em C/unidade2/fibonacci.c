#include <stdio.h>


/* int main(){

   int n;

    int primeiro = 0, segundo = 1, proximo;

    printf("Digite o número de termos da sequência de Fibonacci que você deseja calcular: ");
    scanf("%d", &n);
    
    printf("Sequência de Fibonacci até o termo %d:\n", n);


    for(int i = 0; i < n; i++){
        if(i <= 1){
            proximo = i;
        }else{
            proximo = primeiro + segundo;
            primeiro = segundo;
            segundo = proximo;
        }
    }
*/

#include <stdio.h>

    int main() {

        int i;

        for (i = 0; i < 5; i++) {
            if (i == 2) {
            continue;
        }
        printf("%d ", i);

        }

    return 0;
    }

/*
TERNÁRIO
int main(){
    int num;
    printf("Digite um numero: ");
    scanf("%d", num);

    (num == 10) ? printf("O numero é igual a 10\n") : printf("O numero é diferente de 10.\n");

    return 0;
}


*/