#include <stdio.h>

int main() {
    int a_x, a_y, a_z;
    int b_x, b_y, b_z;
    int c_x, c_y, c_z;
    scanf("%d %d %d", &a_x, &a_y, &a_z);
    scanf("%d %d %d", &c_x, &c_y, &c_z);

    b_x = c_x - a_z;
    if (c_y >= a_y) b_y = c_y / a_y;
    else b_y = a_y / c_y;
    b_z = c_z - a_x;

    printf("%d %d %d\n", b_x, b_y, b_z);
}