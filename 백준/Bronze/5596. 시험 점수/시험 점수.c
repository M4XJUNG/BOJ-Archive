#include <stdio.h>

int main() {
  int s_i, s_m, s_s, s_e, s;
  int t_i, t_m, t_s, t_e, t;
  scanf("%d %d %d %d", &s_i, &s_m, &s_s, &s_e);
  scanf("%d %d %d %d", &t_i, &t_m, &t_s, &t_e);
  s = s_i + s_m + s_s + s_e;
  t = t_i + t_m + t_s + t_e;
  if (s >= t) printf("%d\n", s);
  else printf("%d\n", t);
}