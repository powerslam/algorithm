#include <iostream>
#include <memory.h>
#include <vector>

#define MAX 10000

using namespace std;

int n, m, a, b;
int user[101][101];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

	cin >> n >> m;

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			user[i][j] = MAX;

	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		user[a][b] = user[b][a] = 1;
	}

	for (int k = 1; k <= n; k++) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				if (user[i][j] > user[i][k] + user[k][j]) {
					user[i][j] = user[i][k] + user[k][j];
				}
			}
		}
	}

	int r = MAX;
	int ans = 0;
	for (int i = 1; i <= n; i++) {
		int tmp = 0;
		for (int j = 1; j <= n; j++) {
			if (user[i][j] != MAX) tmp += user[i][j];
		}
		if (r > tmp) ans = i, r = tmp;
	}

	cout << ans;
}