#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>

int n, m, ary[8];
bool visited[8] = { 0 };

void dfs(int cnt){ 
    if (m <= cnt)
    {
        for (int i = 0; i < m; i++) {
            printf("%d ", ary[i]);
        }
        printf("\n");
        return;
    }
    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            ary[cnt] = i;
            visited[i] = 1;
            dfs(cnt + 1);
            visited[i] = 0;
        }
    }
}

int main()
{
    scanf("%d %d", &n, &m);

    dfs(0);

    return 0;
}