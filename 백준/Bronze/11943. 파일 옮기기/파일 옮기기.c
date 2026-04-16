#include <stdio.h>

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    if (a + d <= b + c) printf("%d\n", a + d);
    else printf("%d\n", b + c);
    return 0;
}

// 1 바구니 : 사과 A개 / 오렌지 B개
// 2 바구니 : 사과 C개 / 오렌지 D개

// 1 바구니 : 사과만
// 2 바구니 : 오렌지만

// 과일 옮기는 최소 횟수

