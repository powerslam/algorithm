#include <iostream>
#define MAX 54
using namespace std;
typedef long long ll;

ll a, b, t, ans;
ll cnt[54];

ll maxPos(ll p){
    for(ll i = MAX; i >= 0LL; i--){
        if((p & (1LL << i)) != 0LL)
            return i;
    }

    return 0LL;
}

ll solve(ll p, ll q, ll c){
    ll ret = 0LL, diff = q - p;
    if(diff == 0LL){
        do if(q & 1LL) ret++;
        while(q>>=1LL);
        return ret;
    }
    
    if(!(diff & (diff + 1LL)))
        return cnt[maxPos(diff)] + (diff + 1LL) * c;

    return solve(p, p + (1LL << maxPos(diff)) - 1LL, c) + solve(p + (1LL << maxPos(diff)), q, c + 1LL);
}

int main() {
    cin >> a >> b;
    
    a -= 1LL;
    
    for(ll i = 0LL; i <= MAX; i++) cnt[i] = (i + 1LL) * (1LL << i);

    ll start = solve(0LL, a, 0LL);
    ll end = solve(0LL, b, 0LL);
    cout << end - start << '\n';
}
