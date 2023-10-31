#include <stdio.h>

int main(){
    char c;
    while ((c = getc(stdin)) != EOF) {
        printf("%c", c);
    }
    printf("\?\?!");
}