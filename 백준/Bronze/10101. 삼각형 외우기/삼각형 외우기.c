#include <stdio.h>

int main() {
  int a, b, c, is_triangle = 180;
  scanf("%d %d %d", &a, &b, &c);
  if (a + b + c == is_triangle) {
    if (a == 60 && b == 60 && c == 60) printf("Equilateral\n");
    else if (a == b && b != c) printf("Isosceles\n");
    else if (b == c && c != a) printf("Isosceles\n");
    else if (c == a && a != b) printf("Isosceles\n");
    else if (a != b && b != c) printf("Scalene\n");
  } else printf("Error\n");
}