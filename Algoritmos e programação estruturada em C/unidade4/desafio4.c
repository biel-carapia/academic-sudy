#include <stdio.h>

#include <math.h>

float calcularRaiz(float n, float raizAnt) {

    float raiz = (pow(raizAnt, 2) + n) / (2 * raizAnt);

    if (fabs(raiz - raizAnt) < 0.001)

        return raiz;

    return calcularRaiz(n, raiz);

}

void main() {

    float numero, raiz;

    printf("\nDigite um número para calcular a raiz: ");

    scanf("%f", &numero);

    raiz = calcularRaiz(numero, numero / 2);

    printf("\nRaiz quadrada: %f", raiz);

}

