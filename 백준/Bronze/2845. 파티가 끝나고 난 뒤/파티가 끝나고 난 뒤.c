#include <stdio.h>

int main() {
  int l, p, n[5];
  scanf("%d %d", &l, &p);
  for (int i = 0; i < 5; i++) 
    scanf("%d", &n[i]);
  for (int i = 0; i < 5; i++) {
    if (l * p == n[i]) printf("0 ");
    else printf("%d ", n[i] - l * p);
  }
}