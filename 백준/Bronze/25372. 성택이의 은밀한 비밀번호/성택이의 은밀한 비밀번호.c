#include <stdio.h>
#include <string.h>

int main() {
    int n;
    char pw[20];
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%s", pw);
        if (6 <= strlen(pw) && strlen(pw) <= 9) printf("yes\n");
        else printf("no\n");
    }
}