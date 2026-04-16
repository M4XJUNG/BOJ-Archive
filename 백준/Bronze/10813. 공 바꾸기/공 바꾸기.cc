#include <stdio.h>

int main() {
	int n, m, arr[100] = { 0 };
	scanf("%d %d", &n, &m); // 첫번째 줄 입력 구현.
    
    // 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있는걸 구현
	for (int p = 0; p < n; p++)
		arr[p] = p + 1;
	
	for (int q = 0; q < m; q++) { // 두번째 줄 입력부터 구현.
		int i, j, temp; // 입력할 두 변수 i, j와 교환할 변수 temp 선언
		scanf("%d %d", &i, &j);
		i -= 1; j -= 1; // 1 <= i <= j <= n이므로, - 1을 해야 배열의 0인덱스 접근.
		temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
	for (int i = 0; i < n; i++) 
		printf("%d ", arr[i]);
}