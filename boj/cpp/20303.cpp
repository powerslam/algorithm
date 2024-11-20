#include <map>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;

int n, m, k, a, b;
int dp[30001], uf[30001], sz[30001], candy[30001];

int Find(int p){    
    if(p == uf[p]) return p;
    return uf[p] = Find(uf[p]);
}

void Onion(int p, int q){
    p = Find(p);
    q = Find(q);

    if(p == q) return;

    if(sz[p] < sz[q]){
        uf[p] = q;
        sz[q] += sz[p];
        candy[q] += candy[p];
    } else {
        uf[q] = p;
        sz[p] += sz[q];
        candy[p] += candy[q];
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m >> k;
    for(int i = 1; i <= n; i++){
        cin >> candy[i];
        uf[i] = i;
        sz[i] = 1;
    }

    for(int i = 0; i < m; i++){
        cin >> a >> b;
        Onion(a, b);
    }

    multimap<int, int> m;
    vector<pii> v;
    for(int i = 1; i <= n; i++){
        if(Find(i) == i && sz[i] < k)       
            m.insert(make_pair(sz[i], candy[i]));
    }

    for(auto iter = m.begin(); iter != m.end(); iter++){
        for(int j = k - 1; j >= 1; j--){
            if(iter->first <= j){
                dp[j] = max(dp[j], dp[j - iter->first] + iter->second);
            }
        }
    }

    int ans = 0;
    for(int i = 1; i < k; i++) ans = max(ans, dp[i]);
    cout << ans << '\n';
}
