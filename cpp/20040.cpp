#include <iostream>

using namespace std;

int uf[500001];

int Find(int p) {
    if(p == uf[p]) return p;
    return uf[p] = Find(uf[p]);
}

bool Union(int p, int q) {
    p = Find(p), q = Find(q);
    uf[p] = q;
    return p != q;
}

bool flag;
int n, m, a, b, idx;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;
    for(int i = 0; i < n; i++) uf[i] = i;

    while(m--){
        cin >> a >> b;

        if(!flag) idx++;
        flag |= Union(a, b);
    }

    cout << (flag ? idx : 0) << '\n';
}
