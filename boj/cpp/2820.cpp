#include <iostream>
#include <vector>

using namespace std;

const long long MAXN = 5e5 + 5;
long long n, m;
long long arr[MAXN];
long long cost[MAXN];
vector<long long> adj[MAXN];

long long node_num;
pair<long long, long long> tree_node[MAXN];
vector<long long> tree(4 * MAXN);
vector<long long> lazy(4 * MAXN);

void dfs(long long v) {
    tree_node[v].first = ++node_num;
    for(long long nxt: adj[v])
        dfs(nxt);

    tree_node[v].second = node_num;
}

void init(long long node, long long nl, long long nr) {
    if (nl == nr) {
        tree[node] = cost[nl];
        return;
    }

    long long mid = (nl + nr) >> 1;
    init(node * 2, nl, mid);
    init(node * 2 + 1, mid + 1, nr);
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

void update_lazy(long long node, long long nl, long long nr) {
    if (lazy[node] != 0) {
        tree[node] += (nr - nl + 1) * lazy[node];
        if (nl != nr) {
            lazy[node * 2] += lazy[node];
            lazy[node * 2 + 1] += lazy[node];
        }
        lazy[node] = 0;
    }
}

void update_range(long long node, long long nl, long long nr, long long sl, long long sr, long long diff) {
    update_lazy(node, nl, nr);
    if (sr < nl || nr < sl) return;

    if (sl <= nl && nr <= sr) {
        lazy[node] += diff;
        update_lazy(node, nl, nr);
        return;
    }

    long long mid = (nl + nr) >> 1;
    update_range(node * 2, nl, mid, sl, sr, diff);
    update_range(node * 2 + 1, mid + 1, nr, sl, sr, diff);
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

long long query(long long node, long long nl, long long nr, long long idx) {
    update_lazy(node, nl, nr);
    if (idx < nl || nr < idx) return 0;

    if (nl == nr) return tree[node];

    long long mid = (nl + nr) >> 1;
    return query(node * 2, nl, mid, idx) + query(node * 2 + 1, mid + 1, nr, idx);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;

    cin >> arr[1];
    for (long long i = 1; i < n; i++) {
        long long a, b;
        cin >> a >> b;
        arr[i + 1] = a;
        adj[b].push_back(i + 1);
    }

    dfs(1);

    for(long long i = 1; i <= n; i++)
        cost[tree_node[i].first] = arr[i];

    init(1, 1, n);

    char o;
    for (long long i = 0; i < m; i++) {
        cin >> o;
        if (o == 'p') {
            long long a, b;
            cin >> a >> b;
            if(tree_node[a].first != tree_node[a].second)
                update_range(1, 1, n, tree_node[a].first + 1, tree_node[a].second, b);
        } else {
            long long a;
            cin >> a;
            cout << query(1, 1, n, tree_node[a].first) << '\n';
        }
    }

    return 0;
}
