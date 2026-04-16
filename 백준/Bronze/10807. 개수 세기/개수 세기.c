#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int N, a[100], v = 0, cnt = 0;
	scanf("%d", &N);

	for (int i = 0; i < N; i++)
		scanf("%d ", &a[i]);
	scanf("%d", &v);

	for (int i = 0; i < N; i++)
	{
		if (v == a[i])
			cnt++;
	}
	printf("%d\n", cnt);
	return 0;
}