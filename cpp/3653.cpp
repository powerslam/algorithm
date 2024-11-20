#include <bits/stdc++.h>
using namespace std;

int init(int node, int nl, int nr){
    if(nl == nr){
        if(nl < n){
            tree[node] = 1;
            return 1;
        }

        return 0;
    }

    int mid = nl + nr >> 1;
    return tree[node] = init(node * 2, nl, mid) + init(node * 2, mid + 1, nr);
}

void update(int node, int nl, int nr, int k1, int k2){
    bool next__ = false;
    if(nl <= k1 && k1 <= nr){
        tree[node] -= 1;
        next__ = true;
    }

    if(nl <= k2 && k2 <= nr){
        tree[node] += 1;
        next__ = true;
    }

    if(next__ && nl != nr){
        int mid = nl + nr >> 1;
        update(node * 2, nl, mid, k1, k2);
        update(node * 2 + 1, mid + 1, nr, k1, k2);
    }
}

int query(int node, int nl, int nr, int sl, int sr){
    if(nr < sl || sr < nl)
        return 0;

    if(sl <= nl && nr <= sr)
        return tree[node];

    int mid = nl + nr >> 1;
    return query(node * 2, nl, mid, sl, sr) + query(node * 2 + 1, mid + 1, nr, sl, sr);
}

int n, m, t, tree[800400];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> t;
    while(t--){
        cin >> n >> m;
        memset(tree, 0, sizeof(tree));

        
    }
}
