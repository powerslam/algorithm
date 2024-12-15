#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;

vector<pii> tree_node;
vector<int> adj[200200];
vector<int> arr, colors;
int node_num, mod = 1000000007;
vector<int> tree[800800];

void dfs(int v){
    node_num += 1;
    colors[node_num] = arr[v];
    tree_node[v].first = node_num;

    for(int i = 0; i < adj[v].size(); i++){
        if(tree_node[adj[v][i]].first == 0){
            dfs(adj[v][i]);
        }
    }

    tree_node[v].second = node_num;
}

void init_tree(int node, int nl, int nr){
    if(nl == nr){
        tree[node].push_back(colors[nl]);
        return;
    }

    int mid = nl + nr >> 1;
    init_tree(node * 2, nl, mid);
    init_tree(node * 2 + 1, mid + 1, nr);

    vector<int>(tree[node * 2].size() + tree[node * 2 + 1].size()).swap(tree[node]);
    merge(tree[node * 2].begin(), tree[node * 2].end(), tree[node * 2 + 1].begin(), tree[node * 2 + 1].end(), tree[node].begin());
}

int query(int node, int nl, int nr, int sl, int sr, int key){
    if(sr < nl || nr < sl)
        return 0;

    if(sl <= nl && nr <= sr)
        return upper_bound(tree[node].begin(), tree[node].end(), key) - tree[node].begin();

    int mid = nl + nr >> 1;
    return query(node * 2, nl, mid, sl, sr, key) + query(node * 2 + 1, mid + 1, nr, sl, sr, key);
}

int n, m, c, a, b;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m >> c;
    vector<pii>(n + 1).swap(tree_node);
    vector<int>(n + 1).swap(colors);
    vector<int>(n + 1).swap(arr);

    for(int i = 1; i < n + 1; i++){
        cin >> arr[i];
    }

    for(int i = 0; i < n - 1; i++){
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    dfs(1);

    int ans = 0;
    init_tree(1, 1, n);

    while(m--){
        cin >> a >> b;
        ans = ((ans % mod) + (query(1, 1, n, tree_node[a].first, tree_node[a].second, b) % mod)) % mod;
    }

    cout << ans % mod << '\n';
}
