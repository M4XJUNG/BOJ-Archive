#include <stdio.h>
#include <string.h>

int main() {
    char s[50];
    int n, count = 0;
    scanf("%d", &n);
    scanf("%s", s);
    for (int i = 0; i < n; i++) {
        if (s[i] == 'a' || s[i] == 'i' || s[i] == 'u' || s[i] == 'e' || s[i] == 'o') count++;
    }
    printf("%d\n", count);
}