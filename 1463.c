#include <stdio.h>

int main()
{  
    int N;
    int step = 0;
    int n = 1;

    scanf("%d", &N);

    while (1) {
        n = n * 3;
        ++step;
        if (n > N) {
            --step;
            n = n / 3;
            break;
        }
    }
    
    while (1) {
        n = n * 2;
        ++step;
        if (n > N) {
            --step;
            n = n / 2;
            break;
        }
    }
    
    while (1) {
        ++step;
        n = n + 1;
        if (n > N) {
            --step;
            n = n - 1;
            break;
        }
    }
    
    printf("%d", step);
}