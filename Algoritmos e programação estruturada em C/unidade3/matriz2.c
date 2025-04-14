#include <stdio.h>
#include <stdlib.h>


int main(){

    int matriz[5][5];


    for(int i = 0;i < 5;i++){
        for(int j = 0;j < 5;j++){
            if(i == j){
                matriz[i][j] = 1;
            }else{
                matriz[i][j] = 0;
            }
        }
    }

    printf("Matriz Identidade 5x5:\n");
    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            printf("%d", matriz[i][j]);
        }
        printf("\n");
    }

    return 0;
}

/*

printf("Digite uma nota: ");

scanf("%f", &nota[1][0]);

printf("Nota digitada: %.2f", nota[1][0]);



#include <stdio.h>

int main(){

int matriz[3][3];

int I, j, sDiagPrinc = 0, sDiagSec = 0;

// Leitura da matriz

printf“"Digite os elementos da matriz 3x3:\”");

for (i = 0; i < 3; i++) {

    for (j = 0; j < 3; j++) {

        scanf“"%”", &matriz[i][j]);

    }

}

// Cálculo da soma da diagonal principal e secundária

for (i = 0, j = 2; i < 3, j >=0; i++, j--) {

    sDiagPrinc += matriz[i][i];

    sDiagSec += matriz[i][j];

}

printf“"Soma dos elementos da diagonal principal: %d\”", sDiagPrinc);

printf“"Soma dos elementos da diagonal secundaria: %d\”", sDiagSec);

return 0;

}





#include <stdio.h>

int main() {

    int m, n, p, q, i, j, k;

    int soma = 0;

 

    printf("Digite as dimensões da primeira matriz (m x n): ");

    scanf("%d %d", &m, &n);

    printf("Digite as dimensões da segunda matriz (p x q): ");

    scanf("%d %d", &p, &q);

 

    // Verificação se a multiplicação é possível

    if (n != p) {

        printf("A multiplicação entre as matrizes não é possível.\n");

        return 0;

    }

 

    // Declaração e entrada dos elementos das matrizes

    int matriz1[m][n], matriz2[p][q], resultado[m][q];

    printf("Digite os elementos da primeira matriz:\n");

    for (i = 0; i < m; i++) {

        for (j = 0; j < n; j++) {

            scanf("%d", &matriz1[i][j]);

        }

    }

    printf("Digite os elementos da segunda matriz:\n");

    for (i = 0; i < p; i++) {

        for (j = 0; j < q; j++) {

            scanf("%d", &matriz2[i][j]);

        }

    }

 

    // Cálculo do produto das matrizes

    for (i = 0; i < m; i++) {

        for (j = 0; j < q; j++) {

            for (k = 0; k < p; k++) {

                soma += matriz1[i][k] * matriz2[k][j];

            }

            resultado[i][j] = soma;

            soma = 0;

        }

    }

 

    printf("O produto das matrizes é:\n");

    for (i = 0; i < m; i++) {

        for (j = 0; j < q; j++) {

            printf("%d\t", resultado[i][j]);

        }

        printf("\n");

    }

    return 0;

}


*/