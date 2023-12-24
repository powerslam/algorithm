#include <vector>
#include <iostream>

#define SZ 100001
#define LIM 1000000001

using namespace std;

bool visited[SZ];
int n, r, a, b, l, q;
vector<int> ans(SZ, -1), adj[SZ];

void dfs(int now, bool isMax){
    visited[now] = true;

    int& ret = ans[now];
    if(ret != -1) return;

    ret = isMax ? -LIM : LIM;
    for(int next: adj[now]){
        if(visited[next]) continue;

        dfs(next, !isMax);
        ret = isMax ? max(ret, ans[next]) : min(ret, ans[next]);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> n >> r;

    for(int i = 1; i < n; i++){
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    cin >> l;
    while(l--){
        cin >> a;
        cin >> ans[a];
    }

    dfs(r, true);

    cin >> q;
    while(q--){
        cin >> a;
        cout << ans[a] << '\n';
    }
}
