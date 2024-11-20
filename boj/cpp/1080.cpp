#include <iostream>

using namespace std;

char c;
int n, m, board[51][51], comp[51][51];

void inverse(int y, int x){
    for(int i = y; i < y + 3; i++){
        for(int j = x; j < x + 3; j++){
            board[i][j] = 1 - board[i][j];
        }
    }
}

int main() {
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> c;
            board[i][j] = c - '0';
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> c;
            comp[i][j] = c - '0';
        }
    }

    int ans = 0;
    for(int i = 0; i < n - 2; i++){
        for(int j = 0; j < m - 2; j++){
            if(board[i][j] != comp[i][j]){
                inverse(i, j);
                ans += 1;
            }
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(board[i][j] != comp[i][j]){
                cout << -1  << '\n';
                return 0;
            }
        }
    }

    cout << ans << '\n';
}
