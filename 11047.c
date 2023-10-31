#include <stdio.h>

int main() {
    int N, K, amount = 0, Val[10] = {0, };

    scanf("%d %d", &N, &K);

    for (int i = N; i > 0; i--) {
        scanf(" %d", &Val[i - 1]);
    }

    for (int i = 0; i < N; i++) {
        while (K >= Val[i]) {
            K -= Val[i];
            amount++;
        }
    }
    printf("%d", amount++);
}