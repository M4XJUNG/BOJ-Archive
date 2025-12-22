#include <stdio.h>

int main() {
    int n, new_n, count = 0;
    scanf("%d", &n);
    new_n = n;

    while(1) {
        n = (n / 10 + n % 10) % 10 + (n % 10 * 10);
        count++;
        if (n == new_n)
            break;
    }

    printf("%d\n", count);
}
