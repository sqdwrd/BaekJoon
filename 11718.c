#include <stdio.h>

int main() {
    char a = 0;
    while ((a = getc(stdin)) != EOF) {
        printf("%c", a);
    }
}