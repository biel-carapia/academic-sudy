#include <stdio.h>



int main(){

    int mat[4][3];

    for(i = 0; i < 4; i++){
        for(j = 0; j < 3; j++){
            printf("mat[%d][%d]: ", i, j );
            scanf("%d", &mat[i][j]);
        }
    }

    return 0;
}