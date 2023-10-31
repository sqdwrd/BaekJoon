#include <stdio.h>

int main()
{
    int testN; //테스트 케이스 개수

    scanf("%d", &testN);

    for (int j = 0; j < testN; j++)
    {
        int result = 0;
        int N, M; // N: 책 수, M: 학생 수
        int student[1001][2]; // 학생들이 제출한 신청서
        _Bool taken[1001] = { // 책을 가져갔는지 여부
            0,
        };
        scanf("%d %d", &N, &M);


        for (int i = 0; i < M; i++)
        {
            scanf("%d %d", &student[i][0], &student[i][1]);
        }

        for (int range = 0; range <= N; range++) // 신청한 범위가 작을수록(책을 명확히 고를수록) 먼저 할당
        {
            for (int i = 0; i < M; i++)
            {   
                if (student[i][1] - student[i][0] == range)
                {
                    for (int k = student[i][0]; k <= student[i][1]; k++)
                    {
                        if (!taken[k])
                        {   
                            taken[k] = 1;
                            result++;
                            break;
                        }
                    }
                }
            }
        }
        printf("%d\n", result);
    }
}