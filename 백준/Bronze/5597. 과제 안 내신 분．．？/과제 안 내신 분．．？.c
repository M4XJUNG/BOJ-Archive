#include <stdio.h>

int main() {
    int n[30], print_n[30] = { 0 };
    for (int i = 0; i < 28; i++) {
        scanf("%d", &n[i]);
        print_n[n[i] - 1] = 1;
    }
    for (int i = 0; i < 30; i++) {
        if (print_n[i] == 0)
            printf("%d\n", ++i);
    }
    
}