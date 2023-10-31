#include <stdio.h>

int main() {
    int N, numToFind, amount = 0;
    char v[100] = {0,};
    scanf("%d", &N);
    
    for (int i = 0; i < N; i++) {
        scanf("%d", &v[i]);
    }
    
    scanf("%d", &numToFind);
    
    for (int i = 0; i < N; i++) if(v[i] == numToFind) amount++;
    
    printf("%d", amount);
    
}