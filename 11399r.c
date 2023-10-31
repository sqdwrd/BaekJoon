#include <stdio.h>
#include <stdlib.h>


int compare(const void *a , const void *b) 
{ 
     if( *(int*)a > *(int*)b )
        return 1;
    else if( *(int*)a < *(int*)b )
        return -1;
    else
        return 0;
} 


int main() {
    int N, totalTime;
    int time[1001] = {
        0,
    };
    scanf("%d", &N);

    int queueLen = N;

    for (int i = 0; i < N; i++)
    {
        getc(stdin);
        time[i] = getc(stdin) - 48;
    }

    qsort(time, N, 4, compare);


    for (int i = 0; i < N; i++)
    {
        totalTime = totalTime + queueLen * time[i];
        queueLen--;
    }

    printf("%d", totalTime);
}