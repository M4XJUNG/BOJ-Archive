#include <stdio.h>

int main() {
    int n, a, b;
    scanf("%d %d %d", &n, &a, &b);
    if (a > b) printf("Subway\n");
    else if (a < b) printf("Bus\n");
    else printf("Anything\n");
}