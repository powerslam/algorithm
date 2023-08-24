#include <deque>
#include <iostream>
#include <memory.h>

using namespace std;

typedef pair<int, int> pii;

int r, c, cc;
string mov;
pii jongsu;
int cnt[101][101];
deque<pii> robots;
char board[101][101];

pii dPos[9] = {
    pii(1, -1), pii(1, 0), pii(1, 1),
    pii(0, -1), pii(0, 0), pii(0, 1),
    pii(-1, -1), pii(-1, 0), pii(-1, 1),
};

int distance(const pii& a, const pii& b){
    return abs(a.first - b.first) + abs(a.second - b.second);
}

int main() {
    cin >> r >> c;
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            cin >> board[i][j];
            if(board[i][j] == 'R')
                robots.push_back(pii(i, j));

            else if(board[i][j] == 'I')
                jongsu.first = i, jongsu.second = j;
        }
    }
    cin >> mov;

    for(int i = 0; i < mov.size(); i++){
        // 종수 이동
        cc = mov[i] - '1';
        board[jongsu.first][jongsu.second] = '.';
        jongsu.first += dPos[cc].first;
        jongsu.second += dPos[cc].second;
        
        // 이동 위치가 미친 아두이노랑 겹치면 out
        if(board[jongsu.first][jongsu.second] == 'R'){
            cout << "kraj " << i + 1 << '\n';
            return 0;
        }

        // 아니면 map 업데이트
        board[jongsu.first][jongsu.second] = 'I';

        // 미친 아두이노 이동
        // 순환하면서 조건에 맞으면 다시 넣고 아니면 넣지 않는 방식을 따라야 할 것 같음
        int sz = robots.size();
        memset(cnt, 0, sizeof(cnt));
        
        for(int ro = 0; ro < sz; ro++){
            pii& robot = robots[ro];

            int dist = 987654321, dir_idx = 0;
            for(int i = 0; i < 9; i++){
                if(i == 4) continue;

                int ny = robot.first + dPos[i].first, nx = robot.second + dPos[i].second;
                if(ny < 0 || ny >= r || nx < 0 || nx >= c) continue;

                if(dist > distance(pii(ny, nx), jongsu)){
                    dist = distance(pii(ny, nx), jongsu);
                    dir_idx = i;
                }
            }

            int ny = robot.first + dPos[dir_idx].first, nx = robot.second + dPos[dir_idx].second;
            if(board[ny][nx] == 'I'){
                cout << "kraj " << i + 1 << '\n';
                return 0;
            }

            cnt[ny][nx] += 1;
            // 이 단계에서는 무조건 board 를 점으로
            board[robot.first][robot.second] = '.';
            robot.first = ny;
            robot.second = nx;
        }

        pii robot;
        for(int r = 0; r < sz; r++){
            robot.first = robots.front().first;
            robot.second = robots.front().second;
            robots.pop_front();

            // cnt의 값이 2개 이상이면, 로봇이 겹쳤다는 뜻이니까 continue
            if(cnt[robot.first][robot.second] > 1) continue;

            robots.push_back(robot);
            board[robot.first][robot.second] = 'R';
        }
    }

    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++)
            cout << board[i][j];
        cout << '\n';
    }

    return 0;
}
