#include <stdio.h>

int main() {
    int a, b, c, d, count = 0;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    count += a + b + c + d;
    printf("%d\n%d\n", count / 60, count % 60);
}