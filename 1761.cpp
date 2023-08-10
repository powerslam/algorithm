#include <vector>
#include <iostream>

using namespace std;

typedef pair<int, int> pii;

int n, m, a, b, c, diff, ans, depth[40001];
vector<pii> adj[40001];
bool visited[40001];
pii par[40001][21];

void dfs(int s, int p){
    visited[s] = true;
    for(pii k: adj[s]){
        if(visited[k.first]) continue;

        depth[k.first] += depth[s] + 1;
        par[k.first][0] = pii(s, k.second);
        dfs(k.first, s);
    }    
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    for(int i = 0; i < n - 1; i++){
        cin >> a >> b >> c;
        adj[a].push_back(pii(b, c));
        adj[b].push_back(pii(a, c));
    }

    depth[1] = 1;
    dfs(1, 0);

    for(int j = 1; j < 20; j++){
        for(int i = 1; i <= n; i++){
            par[i][j] = par[par[i][j - 1].first][j - 1];
            par[i][j].second += par[i][j - 1].second;
        }
    }

    cin >> m;
    while(m--){
        cin >> a >> b;

        // p 가 가장 깊도록
        if(depth[b] < depth[a]) swap(a, b);

        ans = 0;
        diff = depth[b] - depth[a];
        for(int i = 20; i >= 0; i--){
            // 만약에 diff랑 q가 같으면 q만큼 올라감
            if((diff & (1 << i)) != 0){
                ans += par[b][i].second;
                b = par[b][i].first;
            }
        }


        if(a != b){
            for(int i = 20; i >= 0; i--){
                if(par[b][i].first != par[a][i].first){
                    ans += par[a][i].second;
                    ans += par[b][i].second;
                    
                    a = par[a][i].first;
                    b = par[b][i].first;
                }
            }

            ans += par[a][0].second;
            ans += par[b][0].second;
        }

        cout << ans << '\n';
    }
}
