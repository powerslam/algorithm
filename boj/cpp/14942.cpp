#include <vector>
#include <iostream>

using namespace std;

typedef pair<int, int> pii;

int n, energy[100001], a, b, c;
vector<pii> adj[100001];
bool visited[100001];
pii par[100001][20];

void dfs(int s){
    visited[s] = true;

    for(pii p: adj[s]){
        if(visited[p.first]) continue;
        
        par[p.first][0] = pii(s, p.second);
        dfs(p.first);
    }
}

int solve(int s) {
    int tar = s, p;

    for(p = 19; p >= 0; p--){
        if(par[tar][p].first && par[tar][p].second <= energy[s]){
            energy[s] -= par[tar][p].second;
            tar = par[tar][p].first;
        }
    }

    return tar;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    for(int i = 1; i <= n; i++) cin >> energy[i];

    for(int i = 0; i < n - 1; i++){
        cin >> a >> b >> c;
        adj[a].push_back(pii(b, c));
        adj[b].push_back(pii(a, c));
    }

    dfs(1);

    for(int i = 1; i < 20; i++){
        for(int j = 2; j <= n; j++){
            par[j][i] = par[par[j][i - 1].first][i - 1];
            par[j][i].second += par[j][i - 1].second;
        }
    }

    cout << 1 << '\n';
    for(int i = 2; i <= n; i++){
        cout << solve(i) << '\n';
    }
}
