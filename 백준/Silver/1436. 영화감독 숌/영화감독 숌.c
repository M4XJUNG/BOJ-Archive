#include <stdio.h>

int check(int a);

int main() {
    int n, num = 0, count = 0;
    scanf("%d", &n);

    while (count < n) {
        num++;
        if (check(num)) count++;
    }

    printf("%d\n", num);
}

int check(int a) {
   while (a >= 666) {
       if (a % 1000 == 666)
           return 1;
       a /= 10;
   }
   return 0;
}
