#include <stdio.h>

int main() {
    int price;
    scanf("%d", &price);

    printf("%d %d\n", (int)(price * 0.78), (int)(price - (price / 5) * 0.22));
}