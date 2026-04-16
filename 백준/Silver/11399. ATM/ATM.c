#include <stdio.h>

void bubble_sort(int arr[], int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
            }
        }
    }
}

int main() {
    int n, P[1001] = { 0 }, count = 0;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &P[i]);
    }
    bubble_sort(P, n);
    for (int i = 1; i <= n; i++) {
        P[i] = P[i - 1] + P[i];
        count += P[i];
    }
    printf("%d\n", count);
}