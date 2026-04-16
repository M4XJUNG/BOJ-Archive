#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int a, b;
	scanf("%d %d", &a, &b);

	if (a > 0 && b > 0)
	{
		printf("1\n");
	}
	else if (a < 0 && b>0)
	{
		printf("2\n");
	}
	else if (a < 0 && b < 0)
	{
		printf("3\n");
	}
	else if (a > 0 && b < 0)
	{
		printf("4\n");
	}
	return 0;
}