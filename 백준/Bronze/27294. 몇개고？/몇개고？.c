#include <stdio.h>

int main() {
    int t, s;
    scanf("%d %d", &t, &s);
    if (s == 1 || (12 > t || t > 16)) printf("%d\n", 280);
    else if (12 <= t && t <= 16 && s == 0) printf("%d\n", 320); 
}