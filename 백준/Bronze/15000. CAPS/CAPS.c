#include <stdio.h>
#include <string.h>

int main() {
    char input[1000000];
    scanf("%s", input);
    int len = strlen(input);
    for (int i = 0; i < len; i++) {
        input[i] -= 32;
        printf("%c", input[i]);
    }
    printf("\n");
}