#include <queue>
#include <vector>
#include <iostream>

using namespace std;

typedef pair<int, int> pii;
typedef pair<pii, int> node;

bool visited[101];
vector<pii> adj[101];
int n, r, a, b, c, d, e;
// 10분 간 기본 요금
// 1분당 추가 요금
int main() {
    cin >> n >> r;

    for(int i = 0; i < r; i++){
        cin >> a >> b >> c >> d >> e;
        if(e > 10) c += (e - 10) * d;
    
        adj[a].push_back(pii(b, c));
    }

    priority_queue<node> q;
    q.push(node(pii(0, 1), 1));

    int ans1 = 987654321, ans2 = 987654321;
    while(!q.empty()){
        int v = q.top().second;
        int cost = -q.top().first.first;
        int cnt = q.top().first.second;
        q.pop();
        
        visited[v] = true;

        if(v == n){
            if(ans1 > cost){
                ans1 = cost;
                ans2 = cnt;
            } else if(ans1 == cost && ans2 > cnt){
                ans1 = cost;
                ans2 = cnt;
            }
            continue;
        }

        for(pii k: adj[v]){
            if(visited[k.first]) continue;
            q.push(node(pii(-cost-k.second, cnt + 1), k.first));
        }
    }

    if(ans1 == 987654321 && ans2 == 987654321)
        cout << "It is not a great way.\n";
    else
        cout << ans1 << ' ' << ans2 << '\n';
}
