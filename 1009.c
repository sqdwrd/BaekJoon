#include <stdio.h>

int main() {
    int T, a, b, r;
    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        scanf(" %d %d", &a, &b);
        r = 1;
        for (int j = 0; j < b; j++) {
            r = (r * a) % 10;
        }
        if (r == 0) r = 10; 
        printf("%d\n", r);
    }
}