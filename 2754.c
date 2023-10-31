#include <stdio.h>

int main() {
    char abcdf, sub;
    float result;
    abcdf = getc(stdin);
    sub = getc(stdin);
    
    switch(abcdf) {
        case 'A':
            result = 4;
            break;
        case 'B':
            result = 3;
            break;
        case 'C':
            result = 2;
            break;
        case 'D':
            result = 1;
            break;
        case 'F':
            result = 0;
            printf("%.1f", result);
            return 0;
    }
    
    switch (sub) {
        case '+':
            result += 0.3;
            break;
        case '-':
            result -= 0.3;
            break;
        case '0':
            break;
    }
    
    printf("%.1f", result);    
}