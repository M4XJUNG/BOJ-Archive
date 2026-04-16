#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	char S[1000] = { 0 };
	int i;
	scanf("%s %d", S, &i);
	printf("%c\n", S[i - 1]);
	return 0;
}