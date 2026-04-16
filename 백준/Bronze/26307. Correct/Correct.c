#include <stdio.h>

int main() {
    int h, m;
    scanf("%d %d", &h, &m);
    if (9 <= h && h <= 11 && 0 <= m && m <= 59) {
        if (h == 9) 
            printf("%d\n", m);
        else 
            printf("%d\n", (h - 9) * 60 + m);
    }
}