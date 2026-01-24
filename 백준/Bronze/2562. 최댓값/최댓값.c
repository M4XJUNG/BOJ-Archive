#include <stdio.h>

int main() {
    int arr[9], max = 0, maxIndex;
    for (int i = 0; i < 9; i++) {
        scanf("%d", &arr[i]);
        if (max < arr[i]) {
            max = arr[i];
            maxIndex = i + 1;
        }
    }
    printf("%d\n%d\n", max, maxIndex);

    return 0;
}