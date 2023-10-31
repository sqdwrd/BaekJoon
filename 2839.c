#include <stdio.h>

int main()
{
    int kg, bag3, bag5;
    scanf("%d", &kg);

    bag5 = kg / 5;
    kg = kg % 5;

    if (kg % 3 == 0)
    {
        bag3 = kg / 3;
        printf("%d", bag3 + bag5);
    }
    else
    {
        if (bag5)
        {
            bag5--;
            kg = kg + 5;
        }

        if (kg % 3 == 0)
        {
            bag3 = kg / 3;
            printf("%d", bag3 + bag5);
        }
        else
        {
            if (bag5)
            {
                bag5--;
                kg = kg + 5;
            }

            if (kg % 3 == 0)
            {
                bag3 = kg / 3;
                printf("%d", bag3 + bag5);
            }
            else
                printf("-1");
        }
    }
}