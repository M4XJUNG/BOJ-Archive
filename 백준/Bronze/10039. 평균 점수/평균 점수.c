#include <stdio.h>

int main() {
    int n[5], sum = 0;
    for (int i = 0; i < 5; i++) {
        scanf("%d", &n[i]);
        if (n[i] < 40) n[i] = 40;
        sum += n[i];
    }
    printf("%d\n", sum / 5);
}