#include <iostream>
#include <algorithm>

using namespace std;

int n, m, k, t, uf[4000001];
int cards[4000001];

int Find(int p){
    if(p == uf[p]) return p;
    return uf[p] = Find(uf[p]);
}

void Union(int p, int q){
    p = Find(p);
    q = Find(q);

    if(p < q) uf[p] = q;
    else uf[q] = p;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m >> k;
    for(int i = 1; i <= n; i++) uf[i] = i;
    for(int i = 0; i < m; i++) cin >> cards[i];
    sort(cards, cards + m);

    while(k--){
        cin >> t;
        int idx = upper_bound(cards, cards + m, t) - cards;
        int par = Find(idx);
        cout << cards[par] << '\n';
        
        Union(par, par + 1);
    }
}
