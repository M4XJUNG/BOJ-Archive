#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int burger[3] = { 0 }, drink[2] = { 0 };
	int cheap_b, cheap_d;
	for (int i = 0; i < 3; i++)
		scanf("%d", &burger[i]);
	for (int j = 0; j < 2; j++)
		scanf("%d", &drink[j]);

	cheap_b = burger[0];
	cheap_d = drink[0];
	for (int i = 0; i < 3; i++)
	{
		if (cheap_b > burger[i])
			cheap_b = burger[i];
	}
	for (int j = 0; j < 2; j++)
	{
		if (cheap_d > drink[j])
			cheap_d = drink[j];
	}
	printf("%d\n", cheap_b + cheap_d - 50);

	return 0;
}