#include <stdio.h>




int fatorial(int n){
    if(n == 0){
        return 1;
    }else{
        return n * fatoral(n -1);
    }
}

int main(){

    fatoral(4);
    fatoral(10);
    fatoral(20);


    return 0;
}