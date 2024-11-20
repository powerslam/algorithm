#include <iostream>

using namespace std;

int g, p, gi, k, ans, uf[100001];
int Find(int p){
    if(p == uf[p]) return p;
    return uf[p] = Find(uf[p]);
}

void Union(int p, int q){
    p = Find(p);
    q = Find(q);

    if(p < q) uf[q] = p;
    else uf[p] = q;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> g >> p;
    for(int i = 0; i <= g; i++) uf[i] = i;

    bool flag = true;
    while(p--){
        cin >> gi;

        k = Find(gi);
        if(flag && k - 1 >= 0){
            Union(k, k - 1);
            ans++;
        }
        else flag = false;
    }

    cout << ans << '\n';
}
