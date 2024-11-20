#include <queue>
#include <string>
#include <vector>
#include <iostream>
#include <memory.h>
#include <fstream>

using namespace std;

struct Node {
    int y, x;
    Node(int y, int x): y(y), x(x){}
};

Node dPos[4] = { Node(-1, 0), Node(0, -1), Node(1, 0), Node(0, 1) };
int t, h, w, ans;
bool visited[100][100], canOpen[26];

int main() {
    ifstream in;
    in.open("D:\\PS\\cpp\\boj\\k.in");
    
    cin >> t;
    while(t--){
        cin >> h >> w;

        string s;
        queue<Node> q;
        char board[100][100];

        memset(visited, false, sizeof(visited));
        memset(canOpen, false, sizeof(canOpen));

        vector<Node> doors[26];

        for(int i = 0; i < h; i++){
            for(int j = 0; j < w; j++){
                cin >> board[i][j];

                if(i == 0 || i == h - 1 || j == 0 || j == w - 1){
                    if(board[i][j] == '$') {
                        visited[i][j] = true;
                        q.push(Node(i, j));
                        ans++;
                    }
                    else if(board[i][j] == '.'){
                        visited[i][j] = true;
                        q.push(Node(i, j));
                    }
                    else if('a' <= board[i][j] && board[i][j] <= 'z'){
                        visited[i][j] = true;
                        q.push(Node(i, j));
                        canOpen[board[i][j] - 'a'] = true;
                    }
                    else if('A' <= board[i][j] && board[i][j] <= 'Z'){
                        doors[board[i][j] - 'A'].push_back(Node(i, j));
                    }
                }
            }
        }

        cin >> s;
        for(int i = 0; s[0] != '0' && i < s.size(); i++){
            canOpen[s[i] - 'a'] = true;
        }

        for(int i = 0; i < h; i++){
            if('A' <= board[i][0] && board[i][0] <= 'Z' && canOpen[board[i][0] - 'A']){
                q.push(Node(i, 0));
            }

            if('A' <= board[i][w - 1] && board[i][w - 1] <= 'Z' && canOpen[board[i][w - 1] - 'A']){
                q.push(Node(i, w - 1));
            }
        }

        for(int i = 0; i < w; i++){
            if('A' <= board[0][i] && board[0][i] <= 'Z' && canOpen[board[0][i] - 'A']){
                q.push(Node(0, i));
            }

            if('A' <= board[h - 1][i] && board[h - 1][i] <= 'Z' && canOpen[board[h - 1][i] - 'A']){
                q.push(Node(h - 1, i));
            }
        }

        while(!q.empty()){
            Node v = q.front(); q.pop();

            for(int i = 0; i < 4; i++){
                int ny = v.y + dPos[i].y, nx = v.x + dPos[i].x;
                
                if(ny < 0 || ny >= h || nx < 0 || nx >= w) continue;
                if(board[ny][nx] == '*') continue;
                if(visited[ny][nx]) continue;

                if('A' <= board[ny][nx] && board[ny][nx] <= 'Z'){
                    if(canOpen[board[ny][nx] - 'A']){
                        visited[ny][nx] = true;
                        q.push(Node(ny, nx));
                    } else {
                        doors[board[ny][nx] - 'A'].push_back(Node(ny, nx));
                    }
                }

                else if('a' <= board[ny][nx] && board[ny][nx] <= 'z'){
                    visited[ny][nx] = true;
                    q.push(Node(ny, nx));
                
                    canOpen[board[ny][nx] - 'a'] = true;

                    for(auto iter = doors[board[ny][nx] - 'a'].begin(); iter != doors[board[ny][nx] - 'a'].end(); iter++){
                        visited[iter->y][iter->x] = true;
                        q.push(*iter);
                    }

                    vector<Node>().swap(doors[board[ny][nx] - 'a']);

                }
                
                else {
                    if(board[ny][nx] == '$') ans++;
                    visited[ny][nx] = true;
                    q.push(Node(ny, nx));
                }
            }
        }

        cout << ans << '\n';
        ans = 0;
    }
}
