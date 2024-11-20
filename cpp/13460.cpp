#include <queue>
#include <iostream>

#define y first
#define x second

using namespace std;

typedef pair<int, int> pos;

int n, m;
char board[11][11];
pos dPos[4] = { {0, 1}, {1, 0}, {-1, 0}, {0, -1} };

pos moveMarble(pos p, int dir){
    bool isRed = board[p.y][p.x] == 'R';

    int ny, nx;
    while(true){
        ny = p.y + dPos[dir].y;
        nx = p.x + dPos[dir].x;

        // 다음 좌표가 벽이면 break
        if(board[ny][nx] == '#') break;

        // 입력으로 준 pos가 빨강이면 다음 좌표가 B 일때 break
        if(isRed && board[ny][nx] == 'B') break;

        // 입력으로 준 pos가 파랑이면 다음 좌표가 R 일때 break
        if(!isRed && board[ny][nx] == 'R') break;

        // 다 통과하면 좌표 갱신
        p.y = ny, p.x = nx;

        // 그런데 다음 좌표가 탈출구면 break
        if(board[ny][nx] == 'O') break;
    }

    // 최종 좌표 return
    return p;
}

void printBoard(){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << board[i][j];
        }
        cout << '\n';
    }
}

int solve(pos r, pos b, int cnt){
    // 만약에 10번째 시도면 out
    if(cnt == 10) return 100;

    // return 값
    int ret = 101;

    // 다음 좌표
    pos nr, nb;

    // 빨간 구슬, 파란 구슬 관계
    int dy = r.y - b.y, dx = r.x - b.x;

    // 만약에 y 좌표 차이가 0이 아니면 나누기
    if(dy != 0) dy /= abs(r.y - b.y);

    // 만약에 x 좌표 차이가 0이 아니면 나누기
    if(dx != 0) dx /= abs(r.x - b.x); 

    // dPos 돌기
    for(int i = 0; i < 4; i++){
        // 만약에 현재 가는 방향이랑 빨강 파랑 관계랑 같으면
        // 왼쪽(0, -1) 가는데, 빨강 파랑 순으로 있는 경우
        // 오른쪽(0, 1) 가는데, 파랑 빨강 순으로 있는 경우
        // 등등
        if(dPos[i].y == dy && dPos[i].x == dx){
            // 다음 좌표로 구하기
            nr = moveMarble(r, i);

            // 파랑 이동할 때 방해하면 안 되니까 미리 이동 시킴
            board[r.y][r.x] = '.';

            // 그런데 이동 시킬 장소가 탈출구가 아니면 이동시킴
            // 탈출구면 R 반영 X
            if(board[nr.y][nr.x] != 'O') board[nr.y][nr.x] = 'R';

            // 다음 좌표 구하기
            nb = moveMarble(b, i);

            // 파랑 이동시키기
            board[b.y][b.x] = '.';
            
            // 이동 시킬 장소가 탈출구가 아니면 이동시킴
            if(board[nb.y][nb.x] != 'O') board[nb.y][nb.x] = 'B';
        } else {
            // 위랑 반대
            nb = moveMarble(b, i);
            board[b.y][b.x] = '.';
            if(board[nb.y][nb.x] != 'O') board[nb.y][nb.x] = 'B';

            nr = moveMarble(r, i);
            board[r.y][r.x] = '.';
            if(board[nr.y][nr.x] != 'O') board[nr.y][nr.x] = 'R';
        }

        // 만약에 파랑이 탈출구에 기어들어가 있으면
        if(board[nb.y][nb.x] == 'O') {
            // 원래 위치에 파랑 두고
            board[b.y][b.x] = 'B';
            
            // 이거는 혹시 빨강이 O에 들어갔을 수도 잇고 아닐 수도 있어서 넣음
            board[r.y][r.x] = 'R';            
            if(board[nr.y][nr.x] != 'O') board[nr.y][nr.x] = '.';
            continue;
        } else if(board[nr.y][nr.x] == 'O') {
            // 위에서 걸러지지 않았으니까
            // 파랑을 원래 위치로 두고
            board[b.y][b.x] = 'B';
            board[nb.y][nb.x] = '.';

            // 빨강도 원래 위치에 둠
            board[r.y][r.x] = 'R';
            return cnt + 1; // 지금까지 움직인거 + 방금 움직인거
        }

        // 만약에 빨강, 파랑 좌표가 그대로면 continue ==> 경우의 수 차단
        if(nr == r && nb == b) continue;

        // 이렇게 다 돌았는데 조건이 맞지 않으면
        // 재귀함
        ret = min(ret, solve(nr, nb, cnt + 1));

        if(nb != b){            
            board[b.y][b.x] = 'B';
            board[nb.y][nb.x] = '.';
        }

        if(nr != r){
            board[r.y][r.x] = 'R';            
            board[nr.y][nr.x] = '.';
        }
    }

    return ret;
}

int main() {
    cin >> n >> m;

    pos r, b;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> board[i][j];
            if(board[i][j] == 'R') r = pos(i, j);
            if(board[i][j] == 'B') b = pos(i, j);
        }
    }

    int ans = solve(r, b, 0);
    cout << (ans <= 10 ? ans : -1) << '\n';
}
