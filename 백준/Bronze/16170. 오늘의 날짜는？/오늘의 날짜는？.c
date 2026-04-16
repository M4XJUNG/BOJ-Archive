#include <stdio.h>
#include <time.h>

int main() {
    time_t timer;
    struct tm* t;
    timer = time(NULL); // 1970년 1월 1일 0시 0분 0초부터 시작하여 현재까지의 초
    t = localtime(&timer); // 포맷팅을 위해 구조체에 넣기

    printf("%d\n", t->tm_year + 1900);
    printf("%d\n", t->tm_mon + 1);
    printf("%d\n", t->tm_mday);
}