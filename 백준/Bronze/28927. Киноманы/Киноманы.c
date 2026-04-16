#include <stdio.h>

int main() {
    int t1, e1, f1, sum1 = 0;
    int t2, e2, f2, sum2 = 0;
    scanf("%d %d %d %d %d %d", &t1, &e1, &f1, &t2, &e2, &f2);
    t1 *= 3; t2 *= 3;
    e1 *= 20; e2 *= 20;
    f1 *= 120; f2 *= 120;
    sum1 = t1 + e1 + f1;
    sum2 = t2 + e2 + f2;
    if (sum1 > sum2) printf("Max\n");
    else if (sum1 < sum2) printf("Mel\n");
    else printf("Draw\n");
}