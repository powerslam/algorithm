#include <queue>
#include <iostream>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pii;

ll n, l, ans;
queue<pii> p, m;
int main() {
    cin >> n;
    for(ll i = 0; i < n; i++){
        cin >> l;
        if(l > 0) p.push(pii(i, l));
        else m.push(pii(i, -l));
    }

    if(m.empty() || p.empty()){
        cout << 0 << '\n';
        return 0;
    }

    while(!m.empty()){
        ll now = abs(p.front().first - m.front().first);
        if(p.front().second < m.front().second){
            now *= p.front().second;
            m.front().second -= p.front().second;
            p.pop();
        }
        else if(p.front().second == m.front().second){
            now *= p.front().second;
            p.pop(); m.pop();
        }
        else {
            now *= m.front().second;
            p.front().second -= m.front().second;
            m.pop();
        }

        ans += now;
    }

    cout << ans << '\n';
}
