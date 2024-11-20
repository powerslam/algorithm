#include <queue>
#include <iostream>

using namespace std;

typedef pair<int, int> pii;

struct node {
    int y, x, cnt;
    node(int y, int x, int cnt): y(y), x(x), cnt(cnt){}
};

pii dPos[8] = {
    {-1, -1}, {-1, 0}, {-1, 1},
    {0, -1}, {0, 1},
    {1, -1}, {1, 0}, {1, 1}
};

vector<pii> v;
int h, w, cnt[1001][1001], board[1001][1001];
char c;

int main() {
    cin >> h >> w;
    for(int i = 0; i < h; i++){
        for(int j = 0; j < w; j++){
            cin >> c;

            if(c != '.'){
                board[i][j] = c - '0';
                v.push_back(pii(i, j)); 
                for(int k = 0, ny, nx; k < 8; k++){
                    ny = i + dPos[k].first;
                    nx = j + dPos[k].second;
                    
                    if(ny < 0 || ny >= h || nx < 0 || nx >= w) continue;
                    cnt[ny][nx] += 1;
                }
            } else board[i][j] = 0;
        }
    }

    queue<node> q;
    for(pii p: v){
        int y = p.first, x = p.second;
        
        if(board[y][x] <= 8 - cnt[y][x]){
            board[y][x] = 0;
            q.push(node(y, x, 1));
        }
    }

    int ans = 0;
    while(!q.empty()){
        int y = q.front().y, x = q.front().x;
        int c = q.front().cnt;
        ans = max(ans, c);
        
        q.pop();

        for(int i = 0; i < 8; i++){
            int ny = y + dPos[i].first, nx = x + dPos[i].second;
            if(!board[ny][nx]) continue;
            
            cnt[ny][nx] -= 1;
            if(board[ny][nx] <= 8 - cnt[ny][nx]){
                board[ny][nx] = 0;
                q.push(node(ny, nx, c + 1));
            }
        }
    }

    cout << ans << '\n';
}
