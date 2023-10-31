#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N, max = 0;
    scanf("%d", &N);
    int **meet = (int **)malloc(sizeof(int *) * N);
    _Bool *taken = (_Bool *)malloc(sizeof(_Bool) * N);

    for (int i = 0; i < N; i++)
    {
        meet[i] = (int *)malloc(sizeof(int) * 2);
        scanf("%d %d", &meet[i][0], &meet[i][1]);
        if (meet[i][1] > max) max = meet[i][1];
    }

    int result = 0;

    for (int range = 0; range <= max; range++)
    {
        for (int i = 0; i < N; i++)
        {
            if (meet[i][1] - meet[i][0] == range)
            {
                for (int k = meet[i][0]; k <= meet[i][1]; k++)
                {
                    if (!taken[k])
                    {   
                        result++;
                        taken[k] = 1;
                        break;
                    }
                }
            }
        }
    }

    printf("%d", result);
}