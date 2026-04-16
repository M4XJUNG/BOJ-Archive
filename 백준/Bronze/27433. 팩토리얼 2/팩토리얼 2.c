#include <stdio.h>

long long fibonacci(long long n) {
    if (n == 0)
        return 1;
    else return n * fibonacci(n-1);
}

int main() {
    long long n;
    scanf("%lld", &n);
    printf("%lld\n", fibonacci(n));
}