#include <stdio.h>

void reverse(int arr[], int start, int end) {
    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

int main() {
    int N, M;
    scanf("%d %d", &N, &M);

    int basket[N];
    for (int i = 0; i < N; i++) {
        basket[i] = i + 1;
    }

    for (int i = 0; i < M; i++) {
        int start, end;
        scanf("%d %d", &start, &end);
        reverse(basket, start - 1, end - 1);
    }

    for (int i = 0; i < N; i++) {
        printf("%d ", basket[i]);
    }
    printf("\n");

    return 0;
}
