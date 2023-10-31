#include <stdio.h>

int main()
{
    int N;
    int time[1001] = {
        0,
    };
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf(" %d", &time[i]);
    }

    int queueLen = N;
    int min_index;
    unsigned int min_time = 0xffffffff;

    int totaltime = 0;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if ((time[j] != 0) && (min_time > time[j]))
            {
                min_time = time[j];
                min_index = j;
            }
        }
        totaltime = min_time * queueLen + totaltime;
        min_time = 0xffffffff;
        time[min_index] = 0;
        queueLen--;
    }

    printf("%d", totaltime);
}