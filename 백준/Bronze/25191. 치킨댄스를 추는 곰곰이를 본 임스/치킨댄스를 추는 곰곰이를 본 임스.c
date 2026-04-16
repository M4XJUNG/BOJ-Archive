#include <stdio.h>

int main() {
    int n, a, b;
    scanf("%d %d %d", &n, &a, &b);
    if (n >= a / 2 + b) printf("%d\n", a / 2 + b);
    else printf("%d\n", n);
}