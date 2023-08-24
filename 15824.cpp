#include <vector>
#include <iostream>
#include <algorithm>

#define MOD 1000000007

using namespace std;
typedef long long ll;

ll ans, n, tmp, cache[300001];

ll _pow(ll k){
    if(cache[k] != 0) return cache[k];

    cache[k >> 1] = _pow(k >> 1);
    cache[k] = (cache[k >> 1] % MOD) * (cache[k >> 1] % MOD) % MOD;
    if(k % 2) 
        cache[k] = (cache[k] % MOD) * 2LL % MOD;

    return cache[k];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cache[0] = 1LL;
    cache[1] = 2LL;

    cin >> n;
    vector<ll> v(n);
    for(auto& i: v) cin >> i;
    sort(v.begin(), v.end());

    for(int i = 0; i < n; i++){
        // 음수 방지를 위해서 MOD를 더하고 나머지를 구한다.
        tmp = v[i] % MOD * (_pow(i) - _pow(n - i - 1) + MOD) % MOD;
        tmp %= MOD;
        ans = (ans + tmp) % MOD;
    }

    cout << ans << '\n';
}
