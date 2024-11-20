#include <iostream>

using namespace std;

int n, m, matrix[101][101], k;
int main() {
    cin >> n>> m;

    for(int t = 0; t < 2; t++){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                cin >> k;
                matrix[i][j] += k;
            }
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << matrix[i][j] << ' ';
        }
        cout << '\n';
    }
}
