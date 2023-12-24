#include <iostream>

using namespace std;

char c;
bool show[11][11];
int n, ans[11][11], dp[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

int main() {
    cin >> n;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++){
            cin >> c;
            if(c == '*'){
                ans[i][j] = -1;
                for(int k = 0, ny, nx; k < 8; k++){
                    ny = i + dp[k][0], nx = j + dp[k][1];
                    if(ny < 0 || ny >= n || nx < 0 || nx >= n) continue;
                    if(ans[ny][nx] < 0) continue;

                    ans[ny][nx] += 1;
                }
            }
        }

    bool flag = false;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++){
            cin >> c;
            if(c == 'x') {
                flag |= (ans[i][j] == -1);
                show[i][j] = true;
            }
            
            else show[i][j] = false;
        }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(flag) {
                if(ans[i][j] == -1) cout << '*';
                else if(!show[i][j]) cout << '.';
                else cout << ans[i][j];
            } else {
                if(ans[i][j] == -2) cout << '.';
                else cout << ans[i][j];
            }
        }
        cout << '\n';
    }
}
