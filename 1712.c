#include <stdio.h>

int main() {
    int A, B, C, Profit, N = 0;
    scanf("%d %d %d", &A, &B, &C);
    Profit = -A;
    if (B >= C) {
        printf("-1");
        return 0;
    }

    // 수익 = (판매가 - 가변비용) * 판매대수 - 고정비용 > 0
    // 판매대수 = (수익 + 고정비용) / (판매가 - 가변비용)
    printf("%d", A / (C-B) + 1);
}