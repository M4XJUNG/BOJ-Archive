#include <stdio.h>

int main() {
    int n, num[1000], even_count = 0, odd_count = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &num[i]);
        if (num[i] % 2 == 0) even_count++;
        else odd_count++;
    }
    if (even_count > odd_count) printf("Happy\n");
    else printf("Sad\n");
}