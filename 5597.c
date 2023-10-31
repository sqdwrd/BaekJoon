#include <stdio.h>

int main() {
    int handin[30] = {0, };
    int num;
    
    for (int i = 0; i < 28; i++) {
        scanf("%d", &num);
        handin[num - 1] = 1;
    }
    
    for (int i = 0; i < 30; i++) {
        if (handin[i] == 0) printf("%d\n", i + 1);
    }
}