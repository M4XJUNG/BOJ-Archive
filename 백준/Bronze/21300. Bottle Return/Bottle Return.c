#include <stdio.h>

int main() {
    int n[6] = { 0 }, sum = 0;
    for (int i = 0; i < 6; i++) {
        scanf("%d", &n[i]);
        sum += n[i] * 5;
    }
    printf("%d\n", sum);
}