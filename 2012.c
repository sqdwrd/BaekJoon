#include <stdio.h>

int main()
{
    int N;
    _Bool A[6] = {
        0,
    };
    int fallback[6] = {
        0,
    };

    int result;

    for (int i = 0; i < N; i++)
    {
        int n;
        scanf("%d", &n);
        if (!A[n])
        {
            A[n] = 1;
        }
        else
        {
            fallback[n]++;
        }
    }

    for (int i = 0; i < N; i++)
    {
        
    }

    printf("%d\n", result);
}