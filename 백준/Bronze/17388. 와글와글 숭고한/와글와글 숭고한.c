#include <stdio.h>

int main() {
    int s, k, h;
    scanf("%d %d %d", &s, &k, &h);
    if (s + k + h >= 100) printf("OK\n");
    else {
        if (s < k && k < h) printf("Soongsil\n");
        else if (s < h && h < k) printf("Soongsil\n");
        else if (k < h && h < s) printf("Korea\n");
        else if (k < s && s < h) printf("Korea\n");
        else if (h < s && s < k) printf("Hanyang\n");
        else if (h < k && k < s) printf("Hanyang\n");
    }
}