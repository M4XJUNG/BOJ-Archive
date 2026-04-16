#include <stdio.h>

int main() {
    int n, m;
    char bung[11][11];

    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++) {
        scanf("%s", bung[i]);
    }

    for (int i = 0; i < n; i++) {
        for (int j = m - 1; j >= 0; j--) {
            printf("%c", bung[i][j]);
        }
        printf("\n");
    }

    return 0;
}