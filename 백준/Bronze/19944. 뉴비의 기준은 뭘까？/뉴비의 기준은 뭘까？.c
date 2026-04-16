#include <stdio.h>

int main() {
    int n, m;
    int newbie, oldbie, tle;
    scanf("%d %d", &n, &m);
    newbie = m == 1 || m == 2;
    oldbie = m <= n && !newbie;
    tle = !newbie || !oldbie;
    if (newbie) printf("NEWBIE!\n");
    else if (oldbie) printf("OLDBIE!\n");
    else if (tle) printf("TLE!\n");
}