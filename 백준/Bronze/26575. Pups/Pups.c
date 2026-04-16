#include <stdio.h>

int main() {
    int n;
    double dog_n, dog_count, food_price;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lf %lf %lf", &dog_n, &dog_count, &food_price);
        printf("$%.2lf\n", dog_n * dog_count * food_price);
    }
}