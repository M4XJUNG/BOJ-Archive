#include <stdio.h>
#include <string.h>

int main() {
    int n, sum, count;
    char string[80];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        sum = 0, count = 1;
        scanf("%s", string);
        for (int j = 0; j < strlen(string); j++) {
            if (string[j] == 'X') count = 1;
            else sum += count++;
        }
        printf("%d\n", sum);
    }
}