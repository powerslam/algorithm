#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;

// t_i 분에 k 번째 차를 마셨을 때 max 효과
int dp[1000001][11];
int cnt[1000001];
int t, n, d, k;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> t >> n >> d >> k;
    vector<int> v(n + 1);

    for(int i = 1; i <= n; i++) cin >> v[i];
    
    sort(v.begin(), v.end());

    int idx, limit;
    for(int i = 1; i <= n; i++){
        limit = v[i] - d + 1;
        idx = lower_bound(v.begin() + 1, v.end(), limit) - v.begin();    
        cnt[i] = i - idx + 1;
    }

    for(int j = 1; j <= k; j++){
        for(int i = 1; i <= n; i++){
            dp[i][j] = max(dp[i - 1][j], cnt[i] + dp[i - cnt[i]][j - 1]);    
        }
    }

    cout << dp[n][k];
}
