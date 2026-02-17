#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int a, b, c;
	int A, B, C;
	
	while (1)
	{
		scanf("%d %d %d", &a, &b, &c);
		A = a * a;
		B = b * b;
		C = c * c;
		if (a == 0 && b == 0 && c == 0)
			break;
		else if (a != 0 && b != 0 && c != 0)
		{
			if (A > B && A > C && A == B + C)
				printf("right\n");
			else if (B > A && B > C && B == A + C)
				printf("right\n");
			else if (C > A && C > B && C == A + B)
				printf("right\n");
			else
				printf("wrong\n");
		}
	}
	return 0;
}