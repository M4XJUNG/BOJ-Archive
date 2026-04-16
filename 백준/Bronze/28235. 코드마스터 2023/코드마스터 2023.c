#include <stdio.h>
#include <string.h>

int main() {
    char name[10];
    scanf("%s", name);
    if (strcmp(name, "SONGDO") == 0) printf("HIGHSCHOOL\n");
    else if (strcmp(name, "CODE") == 0) printf("MASTER\n");
    else if (strcmp(name, "2023") == 0) printf("0611\n");
    else if (strcmp(name, "ALGORITHM") == 0) printf("CONTEST\n");
}