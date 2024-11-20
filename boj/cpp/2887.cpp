#include <queue>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

struct pos {
    int idx;
    ll x, y, z;
    pos(ll x = 0, ll y = 0, ll z = 0): idx(0){
        this->x = x;
        this->y = y;
        this->z = z;
    }
};

struct edge {
    int head, tail;
    ll cost;

    edge(int head, int tail, ll cost) {
        this->head = head;
        this->tail = tail;
        this->cost = cost;
    }
};

int n, cnt;
ll a, b, c;
pos v[100001];
vector<edge> edges;
bool visited[100001];

int parent[1000001];

int _find(int p){
    if(parent[p] == p) return p;
    return parent[p] = _find(parent[p]);
}

void _union(int u, int v){
    u = _find(u);
    v = _find(v);

    parent[v] = u;
}

int main() {
    cin >> n;
    for(int i = 0; i < n; i++){
        v[i].idx = i;
        cin >> v[i].x >> v[i].y >> v[i].z;
        parent[i] = i;
    }

    sort(v, v + n, [](const pos& a, const pos& b) {
        return a.x < b.x;
    });

    for(int i = 1; i < n; i++){
        edges.push_back(edge(v[i - 1].idx, v[i].idx, abs(v[i - 1].x - v[i].x)));
    }

    sort(v, v + n, [](const pos& a, const pos& b) {
        return a.y < b.y;
    });

    for(int i = 1; i < n; i++){
        edges.push_back(edge(v[i - 1].idx, v[i].idx, abs(v[i - 1].y - v[i].y)));
    }

    sort(v, v + n, [](const pos& a, const pos& b) {
        return a.z < b.z;
    });

    for(int i = 1; i < n; i++){
        edges.push_back(edge(v[i - 1].idx, v[i].idx, abs(v[i - 1].z - v[i].z)));
    }

    sort(edges.begin(), edges.end(), [](const edge& a, const edge& b){
        return a.cost < b.cost;
    });

    int cnt = 0, ans = 0;
    for(edge e: edges){
        if(cnt == n - 1) break;
        if(_find(e.head) == _find(e.tail)) continue;

        _union(e.head, e.tail);
        ans += e.cost;
        cnt += 1;
    }

    cout << ans << endl;
}
