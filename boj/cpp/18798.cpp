#include <vector>
#include <iostream>

using namespace std;

struct Node {
    int common, cnt;

    Node(): common(0), cnt(0) {}

    Node(int common, int cnt): 
        common(common), cnt(cnt) {}
};

const int maxN = 250250;

int n, k, m, o, l, r, x;

int arr[maxN];
vector<Node> tree(maxN * 4);

void init(int node, int nl, int nr){
    if (nl == nr){
        tree[node] = Node(arr[nl], (int) (arr[nl] == k));
        return;
    }

    int mid = nl + nr >> 1;
    init(node * 2, nl, mid);
    init(node * 2 + 1, mid + 1, nr);

    tree[node].common = tree[node * 2].common & tree[node * 2 + 1].common;
    tree[node].cnt = tree[node * 2].cnt + tree[node * 2 + 1].cnt;
}

void update(int node, int nl, int nr, int sl, int sr, int v){
    if(nr < sl || sr < nl) return;
    
    if(nl == nr){
        tree[node].common |= v;
        tree[node].cnt = (int) (tree[node].common == k);
        return;
    }

    if(sl <= nl && nr <= sr){
        if((tree[node].common | v) == tree[node].common){
            return;
        }
    }

    int mid = nl + nr >> 1;

    update(node * 2, nl, mid, sl, sr, v);
    update(node * 2 + 1, mid + 1, nr, sl, sr, v);

    tree[node].common = tree[node * 2].common & tree[node * 2 + 1].common;
    tree[node].cnt = tree[node * 2].cnt + tree[node * 2 + 1].cnt;
}

int query(int node, int nl, int nr, int sl, int sr){
    if (nr < sl || sr < nl) 
        return 0;
    
    if(sl <= nl && nr <= sr)
        return tree[node].cnt;

    int mid = nl + nr >> 1;
    return query(node * 2, nl, mid, sl, sr) + query(node * 2 + 1, mid + 1, nr, sl, sr);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> k;
    for(int i = 0; i < n; i++) cin >> arr[i];
    
    init(1, 0, n - 1);

    cin >> m;
    while(m--){
        cin >> o;
        if(o == 1){
            cin >> l >> r >> x;
            update(1, 0, n - 1, l - 1, r - 1, x);
        } 
        
        else {
            cin >> l >> r;
            cout << query(1, 0, n - 1, l - 1, r - 1) << '\n';
        }
    }
}
