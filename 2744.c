#include <stdio.h>

int main() {
    char str[100];
    
    scanf("%s", &str);
    
    for (int i = 0; i < 100; i++) {
        if (str[i] == 0) break;
        else if (str[i] >= 65 && str[i] <=90) printf("%c", str[i] + 32);
        else if (str[i] >= 97 && str[i] <=122) printf("%c", str[i] - 32);
    }
}