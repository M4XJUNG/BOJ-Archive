#include <stdio.h>

int main() {
    int regularBox, smallBox;
    scanf("%d %d", &regularBox, &smallBox);
    printf("%d\n", (regularBox * 8 + smallBox * 3) - 28);
}