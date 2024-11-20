#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int uf[100001];

int Find(int p){
    if(uf[p] == p) return p;
    return uf[p] = Find(uf[p]);
}

void Union(int p, int q){
    p = uf[p];
    q = uf[q];

    uf[p] = q;
}

struct Edge {
    int a, b, c;
    Edge(int a, int b, int c): a(a), b(b), c(c){}
};

vector<Edge> edges;
int n, m, a, b, c;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cin.tie(NULL);

    cin >> n >> m;

    for(int i = 0; i < n; i++) uf[i] = i;

    for(int i = 0; i < m; i++){
        cin >> a >> b >> c;
        edges.push_back(Edge(a, b, c));
    }

    sort(edges.begin(), edges.end(), [](Edge& a, Edge& b){
        return a.c < b.c;
    });

    int ans = 0, maxCost = 0;
    for(Edge e: edges){
        if(Find(e.a) == Find(e.b)) continue;

        Union(e.a, e.b);
        maxCost = max(maxCost, e.c);
        ans += e.c;
    }

    cout << ans - maxCost << endl;
}
