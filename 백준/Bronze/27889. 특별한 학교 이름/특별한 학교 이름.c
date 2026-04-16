#include <stdio.h>
#include <string.h>

int main() {
    char name[10];
    scanf("%s", name);
    if (strcmp(name, "NLCS") == 0) printf("North London Collegiate School\n");
    else if (strcmp(name, "BHA") == 0) printf("Branksome Hall Asia\n");
    else if (strcmp(name, "KIS") == 0) printf("Korea International School\n");
    else if (strcmp(name, "SJA") == 0) printf("St. Johnsbury Academy\n");
}