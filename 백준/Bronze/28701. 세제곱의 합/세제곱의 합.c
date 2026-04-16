#include <stdio.h>

int main() {
    int n_1, n_2, n_3 = 0, sum = 0;
    scanf("%d", &n_1);
    for (int i = 0; i < n_1; i++) {
        sum += i + 1;
        n_2 = sum * sum;
        n_3 += (i + 1) * (i + 1) * (i + 1);
    }
    printf("%d\n%d\n%d\n", sum, n_2, n_3);
}