#include <iostream>

#define MAX 1000001

using namespace std;

char c;
int n, m, k, ans;
int uf[MAX];

int red(int y, int x){
    return y * m + x;
}

int Find(int p){
    if(uf[p] == p) return p;

    return uf[p] = Find(uf[p]);
}

int Union(int p, int q){
    p = Find(p);
    q = Find(q);

    if(p == q) return 0;
    
    uf[p] = q;
    return 1;
}

int main() {
    for(int i = 0; i < MAX; i++) uf[i] = i;

    cin >> n >> m;
    ans = n * m;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> c;
            if(c == 'L') k = Union(red(i, j), red(i, j - 1));
            else if(c == 'R') k = Union(red(i, j), red(i, j + 1));
            else if(c == 'U') k = Union(red(i, j), red(i - 1, j));
            else k = Union(red(i, j), red(i + 1, j));
        
            ans -= k;
        }
    }

    cout << ans << '\n';
}
