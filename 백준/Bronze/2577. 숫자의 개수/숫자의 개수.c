#include <stdio.h>

int main() {
    int a, b, c, mul, num, n[10] = { 0 };
    scanf("%d %d %d", &a, &b, &c);
    mul = a * b * c;

    while(1) {
        num = mul % 10;
        n[num]++;
        mul /= 10;
        if (mul == 0) break;
    }
    for (int i = 0; i < 10; i++) {
        printf("%d\n", n[i]);
    }
}