#include <map>
#include <iostream>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;

int t, n, m, A[1010], B[1010], i, j;
map<int, int> mA, mB;

int main(){
    cin >> t >> n;
    for(i = 1; i <= n; i++){
        cin >> A[i];
        A[i] += A[i - 1];
    }

    cin >> m;
    for(i = 1; i <= m; i++){
        cin >> B[i];
        B[i] += B[i - 1];
    }

    for(i = 0; i <= n; i++){
        for(j = i + 1; j <= n; j++){
            mA[A[j] - A[i]] += 1;
        }
    }

    for(i = 0; i <= m; i++){
        for(j = i + 1; j <= m; j++){
            mB[B[j] - B[i]] += 1;
        }
    }

    ll ans = 0LL;
    for(auto iter = mA.begin(); iter != mA.end(); iter++){
        ans += 1LL * iter->second * mB[t - iter->first];
    }

    cout << ans << '\n';
}
