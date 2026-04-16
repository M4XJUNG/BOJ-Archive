/*
01 02 03 04 05
09 08 07 06
   10 11 12 13
17 16 15 14
   18 19 20 21
25 24 23 22

01 09 17 25 ... 1001
05 13 21 29 

   125
8 1000
   8
   200
   160
    40
*/
#include <stdio.h>

int main() {
    unsigned int n;
    scanf("%u", &n);
    if (n % 8 == 1) printf("%d\n", 1);
    else if (n % 8 == 5) printf("%d\n", 5);
    else if (n % 8 == 2 || n % 8 == 0) printf("%d\n", 2);
    else if (n % 8 == 3 || n % 8 == 7) printf("%d\n", 3);
    else if (n % 8 == 4 || n % 8 == 6) printf("%d\n", 4);
}