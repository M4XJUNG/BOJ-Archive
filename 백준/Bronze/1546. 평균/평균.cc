#include <stdio.h>

int main() {
	int n;
	double score[1000] = { 0.0 }, max = 0.0, sum = 0.0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%lf", &score[i]);

	for (int i = 0; i < n; i++) {
		if (max < score[i])
			max = score[i];
	}
	for (int i = 0; i < n; i++) {
		score[i] = score[i] / max * 100;
		sum += score[i];
	}
	printf("%.2lf", sum / n);
}