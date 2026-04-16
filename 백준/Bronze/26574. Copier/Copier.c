#include <stdio.h>

int main() {
    int n, num;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &num);
        printf("%d %d\n", num, num);
    }
}