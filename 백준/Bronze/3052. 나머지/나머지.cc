#include <stdio.h>

int main() {
    int n[10], print_n[42] = { 0 }, count = 0;
    for (int i = 0; i < 10; i++) {
        scanf("%d", &n[i]);
        print_n[n[i] % 42] = 1;
    }
    for (int i = 0; i < 42; i++) {
        if (print_n[i] == 1)
            count++;
    }
    printf("%d", count);
}