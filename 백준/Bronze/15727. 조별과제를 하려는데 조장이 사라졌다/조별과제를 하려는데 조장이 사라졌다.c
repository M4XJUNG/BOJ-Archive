#include <stdio.h>

int main() {
    int L;
    scanf("%d", &L);
    if (L % 5 == 0) printf("%d\n", L / 5);
    else printf("%d\n", L / 5 + 1);
}