#include <stdio.h>

int main() {
    int n, x, y;
    int q1_num, q2_num, q3_num, q4_num, axis;
    q1_num = q2_num = q3_num = q4_num = axis = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &x, &y);
        if (x > 0 && y > 0) q1_num++;
        else if (x < 0 && y > 0) q2_num++;
        else if (x < 0 && y < 0) q3_num++;
        else if (x > 0 && y < 0) q4_num++;
        else axis++;
    }
    printf("Q1: %d\n", q1_num);
    printf("Q2: %d\n", q2_num);
    printf("Q3: %d\n", q3_num);
    printf("Q4: %d\n", q4_num);
    printf("AXIS: %d\n", axis);
}