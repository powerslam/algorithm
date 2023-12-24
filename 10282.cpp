#include <vector>
#include <queue>
#include <iostream>

#define INF 987654321

using namespace std;

typedef pair<int, int> pii;

int t, n, d, c, a, b, s, ans;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> t;
    while(t--){
        ans = INF;
        cin >> n >> d >> c;

        int cnt = 0, Mdst = 0;
        priority_queue<pii> q;
        vector<vector<pii>> adj(n + 1);
        vector<int> dist(n + 1, INF);

        for(int i = 0; i < d; i++){
            cin >> a >> b >> s;
            adj[b].push_back(pii(a, s));
        }

        cnt = 1;
        dist[c] = 0;
        q.push(pii(0, c));

        while(!q.empty()){
            int dst = -q.top().first;
            int vx = q.top().second;
            q.pop();

            for(pii p: adj[vx]){
                int nvx = p.first;
                int ndst = p.second + dst;

                if(ndst < dist[nvx]){
                    dist[nvx] = ndst;
                    q.push(pii(-ndst, nvx));
                }
            }
        }

        for(int d: dist){
            if(d == INF) continue;
            cnt += 1;
            Mdst = max(Mdst, d);
        }

        cout << cnt - 1 << ' ' << Mdst << '\n';
    }
}
