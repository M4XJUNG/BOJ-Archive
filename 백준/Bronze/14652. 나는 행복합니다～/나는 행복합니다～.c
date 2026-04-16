#include <stdio.h>

int main() {
    int n, m, k, count = 0;
    scanf("%d %d %d", &n, &m, &k);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (count == k) {
                printf("%d %d\n", i, j);
                return 0;
            }
            count++;
        }
    }
}