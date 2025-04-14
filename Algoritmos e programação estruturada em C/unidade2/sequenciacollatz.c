#include <stdlib.h>

int main() {

    int num, i;

    printf("\n\nDigite um numero:\n");
    scanf("%d", &num);

    i = 0;

    while (num > 1) {
        if (num % 2 == 0)
            num /= 2;
        else
            num = 3 * num + 1;
            printf("\n%d\n", num);
            i++;
    }

    return 0;

}