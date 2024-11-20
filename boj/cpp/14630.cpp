#include <queue>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

typedef pair<int, int> pii;

string s;
bool visited[1001][1001];
int adm[1001][1001];
int n, m, part[1001][101], now, want;

int cost(int i, int j){
    int res = 0;
    for(int k = 0; k < m; k++){
        res += (part[i][k] - part[j][k]) * (part[i][k] - part[j][k]);
    }

    return res;
}

void bfs(){
    priority_queue<pii> q;
    q.push(pii(0, now));

    while(!q.empty()){
        pii p = q.top(); q.pop();
        int cost = -p.first, v = p.second;
        
        if(v == want){
            cout << cost << '\n';
            return;
        }

        for(int i = 0; i < n; i++){
            if(v == i) continue;
            if(visited[v][i]) continue;

            visited[v][i] = visited[i][v] = true;
            q.push(pii(-cost-adm[v][i], i));
        }
    }
}

int main() {
    cin >> n;

    for(int i = 0; i < n; i++){
        cin >> s;
        
        m = s.size();
        for(int j = 0; j < m; j++){
            part[i][j] = s[j] - '0';
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            adm[i][j] = adm[j][i] = cost(i, j);
        }
    }

    cin >> now >> want;
    now -= 1; want -= 1;

    bfs();
}
