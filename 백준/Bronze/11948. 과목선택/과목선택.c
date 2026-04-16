#include <stdio.h>

int main() {
    int science[4], society[2], min_sc = 100, min_so = 100, sum = 0;
    for (int i = 0; i < 4; i++) {
        scanf("%d", &science[i]);
        if (min_sc > science[i]) min_sc = science[i];
        sum += science[i];
    }
    for (int i = 0; i < 2; i++) {
        scanf("%d", &society[i]);
        if (min_so > society[i]) min_so = society[i];
        sum += society[i];
    }
    sum = sum - min_sc - min_so;
    printf("%d\n", sum);    
}