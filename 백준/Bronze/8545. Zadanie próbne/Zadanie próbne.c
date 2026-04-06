#include <stdio.h>

int main() {
    char n[3];
    scanf("%s", n);
    for (int i = 2; i >= 0; i--) {
        printf("%c", n[i]);
    }
}