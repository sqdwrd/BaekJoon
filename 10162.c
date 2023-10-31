#include <stdio.h>

int main() {
    int T, A = 0, B = 0, C = 0;
    scanf("%d", &T);

    // A = 300
    while (T >= 300) {
        A++;
        T -= 300;
    }

    // B = 100
    while (T >= 60) {
        B++;
        T -= 60;
    }

    // C = 10
    while (T >= 10) {
        C++;
        T -= 10;
    }

    (T == 0)? printf("%d %d %d", A, B, C): printf("-1");
}