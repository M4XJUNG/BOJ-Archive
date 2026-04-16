#include <stdio.h>

int main() {
    int n, m, print_arr[100] = { 0 };
    scanf("%d %d", &n, &m);
    
    for (int p = 0; p < m; p++) {
        int i, j, k;
        scanf("%d %d %d", &i, &j, &k);
        for (int q = i - 1; q < j; q++) {
            print_arr[q] = k;
        }
    }
    for (int i = 0; i < n; i++) {
        printf("%d ", print_arr[i]);
    }
}