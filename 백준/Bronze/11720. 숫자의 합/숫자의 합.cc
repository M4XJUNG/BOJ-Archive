#include <stdio.h>
#include <string.h>

int main() {
    int n1, sum = 0;
    char n[100];
    scanf("%d", &n1);
    scanf("%s", n);
    if (n1 == strlen(n)) {
        for (int i = 0; i < n1; i++) {
            int digit = n[i] - '0'; // 문자를 정수로 변환합니다. ('0'을 빼줌으로써)
            sum = sum + digit;
        }
    }
    printf("%d\n", sum);
}
