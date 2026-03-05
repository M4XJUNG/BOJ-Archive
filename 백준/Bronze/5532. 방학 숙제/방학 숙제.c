#include <stdio.h>

int main() {
  int l, a, b, c, d;
  int mat, kor;
  scanf("%d %d %d %d %d", &l, &a, &b, &c, &d);
  if (a % c == 0) mat = a / c;
  else mat = a / c + 1;
  if (b % d == 0) kor = b / d;
  else kor = b / d + 1;
  if (mat > kor) printf("%d\n", l - mat);
  else printf("%d\n", l - kor);
}