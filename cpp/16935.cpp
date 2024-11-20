#include <iostream>

using namespace std;

int n, m, r, o, t, matrix[101][101], _copy[101][101];

void calc1() {
    for(int i = 0; i < n / 2; i++){
        for(int j = 0; j < m; j++){
            t = matrix[n - i - 1][j];
            matrix[n - i - 1][j] = matrix[i][j];
            matrix[i][j] = t;
        }
    }
}

void calc2() {
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m / 2; j++){
            t = matrix[i][m - j - 1];
            matrix[i][m - j - 1] = matrix[i][j];
            matrix[i][j] = t;
        }
    }
}

void calc3() {
    t = n; n = m; m = t;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            _copy[i][j] = matrix[m - j - 1][i];
        }
    }

    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            matrix[i][j] = _copy[i][j];
}

void calc4() {
    t = n; n = m; m = t;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            _copy[i][j] = matrix[j][n - i - 1];
        }
    }

    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            matrix[i][j] = _copy[i][j];
}

void calc5() {
    for(int i = 0; i < n / 2; i++){
        // 4 -> 1
        // 1
        for(int j = 0; j < m / 2; j++){
            _copy[i][j] = matrix[i + n / 2][j];
        }

        // 1 -> 2
        // 2
        for(int j = m / 2; j < m; j++){
            _copy[i][j] = matrix[i][j - m / 2];
        }
    }

    for(int i = n / 2; i < n; i++){
        // 3 -> 4
        for(int j = 0; j < m / 2; j++){
            _copy[i][j] = matrix[i][j + m / 2];
        }

        // 2 -> 3
        for(int j = m / 2; j < m; j++){
            _copy[i][j] = matrix[i - n / 2][j];
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            matrix[i][j] = _copy[i][j];
        }
    }
}

void calc6() {
    for(int i = 0; i < n / 2; i++){
        // 2 -> 1
        for(int j = 0; j < m / 2; j++){
            _copy[i][j] = matrix[i][j + m / 2];
        }

        // 3 -> 2
        for(int j = m / 2; j < m; j++){
            _copy[i][j] = matrix[i + n / 2][j];
        }
    }

    for(int i = n / 2; i < n; i++){
        // 1 -> 4
        for(int j = 0; j < m / 2; j++){
            _copy[i][j] = matrix[i - n / 2][j];
        }

        // 4 -> 3
        for(int j = m / 2; j < m; j++){
            _copy[i][j] = matrix[i][j - m / 2];
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            matrix[i][j] = _copy[i][j];
        }
    }
}

int main(){
    cin >> n >> m >> r;

    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            cin >> matrix[i][j];

    while(r--){
        cin >> o;
        if(o == 1) calc1();
        else if(o == 2) calc2();
        else if(o == 3) calc3();
        else if(o == 4) calc4();
        else if(o == 5) calc5();
        else calc6();
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << matrix[i][j] << ' ';
        }
        cout << '\n';
    }
}
