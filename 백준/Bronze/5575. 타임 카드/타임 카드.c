/*
a[3] a[4] a[5]
a[0] a[1] a[2]
*/

#include <stdio.h>

int main() {
    int a[6];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 6; j++) {
            scanf("%d", &a[j]);
        }
        if (a[5] < a[2]) {
            a[4]--;
            a[5] += 60;
        }
        if (a[4] < a[1]) {
            a[3]--;
            a[4] += 60;
        }
        printf("%d %d %d\n", a[3] - a[0], a[4] - a[1], a[5] - a[2]);
    }
}