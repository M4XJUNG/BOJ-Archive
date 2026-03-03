#include <stdio.h>
#include <string.h>

int main() {
    int n;
    char Si[21];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", Si);
        for (int j = 0; j < strlen(Si); j++) {
            if (Si[j] <= 90) Si[j] += 32;
            printf("%c", Si[j]);
        }
        printf("\n");
    }
}