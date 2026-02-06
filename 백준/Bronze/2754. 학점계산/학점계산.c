#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	char score, num;
	scanf("%c%c", &score, &num);

	if (score == 'A')
		if (num == 43)
			printf("4.3\n");
		else if (num == 45)
			printf("3.7\n");
		else
			printf("4.0\n");
	else if (score == 'B')
		if (num == 43)
			printf("3.3\n");
		else if (num == 45)
			printf("2.7\n");
		else
			printf("3.0\n");
	else if (score == 'C')
		if (num == 43)
			printf("2.3\n");
		else if (num == 45)
			printf("1.7\n");
		else
			printf("2.0\n");
	else if (score == 'D')
		if (num == 43)
			printf("1.3\n");
		else if (num == 45)
			printf("0.7\n");
		else
			printf("1.0\n");
	else
		printf("0.0\n");
}