#include <stdio.h>
#include <limits.h>

int main() {
    int n, arr[1000000];
    int min = INT_MAX, max = INT_MIN;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (min > arr[i]) min = arr[i];
        if (max < arr[i]) max = arr[i];
    }
    printf("%d %d\n", min, max);

    return 0;
}