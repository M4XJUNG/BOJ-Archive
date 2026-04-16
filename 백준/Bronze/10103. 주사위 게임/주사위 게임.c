#include <stdio.h>

int main() {
    int n, ckd, tkd, ckd_score, tkd_score;
    scanf("%d", &n);
    ckd_score = tkd_score = 100;
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &ckd, &tkd);
        if (ckd > tkd) tkd_score -= ckd;
        else if (ckd < tkd) ckd_score -= tkd;
    }
    printf("%d\n%d\n", ckd_score, tkd_score);
}