#include <stdio.h>

int main() {
    int num, n[5], count = 0;
    scanf("%d", &num);
    for (int i = 0; i < 5; i++) {
        scanf("%d", &n[i]);
        if (num == n[i]) count++;
    }
    printf("%d\n", count);
}