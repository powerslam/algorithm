#include <iostream>
#include <queue>

#define Y first
#define X second

using namespace std;

typedef pair<int, int> pii;

int r, c, s, w;
int dy[] = {-1, 0, 1, 0}, dx[] = {0, 1, 0, -1};
char board[251][251];
bool visited[251][251];

pii bfs(pii s){
    pii res;
    queue<pii> q; q.push(s);

    visited[s.Y][s.X] = true;
    if(board[s.Y][s.X] == 'v') res.second++;
    if(board[s.Y][s.X] == 'o') res.first++;

    while(!q.empty()){
        pii v = q.front(); q.pop();

        for(int i = 0; i < 4; i++){
            int ny = v.Y + dy[i], nx = v.X + dx[i];

            if(ny < 0 || ny >= r || nx < 0 || nx >= c) continue;

            if(visited[ny][nx]) continue;
            if(board[ny][nx] == '#') continue;

            if(board[ny][nx] == 'o') res.first++;
            if(board[ny][nx] == 'v') res.second++;

            visited[ny][nx] = true;
            q.push(pii(ny, nx));
        }
    }

    // 늑대가 양보다 적으면 늑대 X
    if(res.second < res.first) res.second = 0;

    // 늑대가 1마리 이상 있는데, 그 수가 양보다 많거나 같은 경우
    else if(res.second != 0) res.first = 0;

    return res;
}

int main(){
    cin >> r >> c;
    for(int i = 0; i < r; i++) for(int j = 0; j < c; j++)
            cin >> board[i][j];

    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            if(!visited[i][j] && board[i][j] != '#'){
                pii res = bfs(pii(i, j));
                //cout << res.first << ' ' << res.second << '\n';
                s += res.first;
                w += res.second;
            }
        }
    }
    cout << s << ' ' << w << '\n';
}
