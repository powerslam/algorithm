#include <iostream>
#include <queue>
#include <set>

#include <memory.h>

#define Y first
#define X second

using namespace std;

typedef pair<int, int> pos;

const pos dpos[4] = {
    {0, 1}, {1, 0}, {0, -1}, {-1, 0}
};

int n, m, board[1001][1001], dp[1001][1001], ans;
bool visited[1001][1001];
int uf[1000001];
string s;

int to1d(int y, int x) {
    return y * m + x;
}

int _find(int p){
    if(uf[p] == p) return p;
    return uf[p] = _find(uf[p]);
}

void _union(int p, int q) {
    p = _find(p);
    q = _find(q);

    uf[q] = p;
}

void bfs(int y, int x){
    queue<pos> q;
    q.push(pos(y, x));
    visited[y][x] = true;

    while(!q.empty()){
        pos v = q.front(); q.pop();

        for(int i = 0; i < 4; i++){
            int ny = v.Y + dpos[i].Y, nx = v.X + dpos[i].X;
            
            if(ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
            if(board[ny][nx]) continue;
            if(visited[ny][nx]) continue;

            dp[y][x] += 1;
            visited[ny][nx] = true;
            q.push(pos(ny, nx));
            _union(to1d(y, x), to1d(ny, nx));
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;
    for(int y = 0; y < n; y++){
        cin >> s;
        for(int x = 0; x < m; x++){
            board[y][x] = s[x] - '0';
            uf[to1d(y, x)] = to1d(y, x);
        }
    }

    for(int y = 0; y < n; y++){
        for(int x = 0; x < m; x++){
            if(board[y][x]) continue;
            if(visited[y][x]) continue;

            dp[y][x] += 1;
            bfs(y, x);
        }
    }

    for(int y = 0; y < n; y++){
        for(int x = 0; x < m; x++){
            if(!board[y][x]) {
                cout << 0;
                continue;
            }

            ans = 1;
            set<int> s;
            //memset(visited, false, sizeof(visited));
            
            for(int i = 0; i < 4; i++){
                int ny = y + dpos[i].Y, nx = x + dpos[i].X;

                if(ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
                if(board[ny][nx]) continue;
                int par = _find(to1d(ny, nx));

                int py = par / m, px = par % m;
                if(s.find(to1d(py, px)) != s.end()) continue;
                
                s.insert(to1d(py, px));
                ans += dp[py][px];
            }

            cout << ans % 10;
        }
        cout << '\n';
    }
}
