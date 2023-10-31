#include <stdio.h>


int main() {
    char T, str[1000];
    int j;
    scanf("%d", &T);
    
    for (int i = 0; i < T; i++) {
        scanf("%s", &str);
        printf("%c", str[0]);
        for (j = 0; str[j] != 0; j++);
        printf("%c\n", str[j-1]);
    }
}