#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int N, pac = 1;
	scanf("%d", &N);

	for (int i = N; i > 0; i--)
	{
		pac *= i;
	}
	printf("%d\n", pac);

	return 0;
}