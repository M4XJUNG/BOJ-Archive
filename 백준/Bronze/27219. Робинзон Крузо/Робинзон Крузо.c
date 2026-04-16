#include <stdio.h>

int main() {
    int n, v, i;
    scanf("%d", &n);
    v = n / 5;
    i = n % 5;
    for (int j = 0; j < v; j++)
        printf("V");
    for (int k = 0; k < i; k++)
        printf("I");
    printf("\n");
}