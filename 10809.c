#include <stdio.h>

int main() {
    char str[100];
    int alpbet[26];

    for (int i = 0; i < 26; i++) {
        alpbet[i] = -1;
    }

    scanf("%s", &str);
    
    for (int i = 0; i < 100; i++) {
        if (!str[i]) break;
        if (alpbet[str[i] - 97] != -1) continue;
        alpbet[str[i] - 97] = i;
    }
    
    for (int i = 0; i < 26; i++) {
        printf("%d ", alpbet[i]);
    }
}