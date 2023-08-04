#include <iostream>

#define MOD 1000000007

using namespace std;

typedef long long ll;

ll d, adj[8][8], res[8][8];
const ll one[8][8] = {
    {0, 1, 1, 0, 0, 0, 0, 0},
    {1, 0, 1, 1, 0, 0, 0, 0},
    {1, 1, 0, 1, 1, 0, 0, 0},
    {0, 1, 1, 0, 1, 1, 0, 0},
    {0, 0, 1, 1, 0, 1, 0, 1},
    {0, 0, 0, 1, 1, 0, 1, 0},
    {0, 0, 0, 0, 0, 1, 0, 1},
    {0, 0, 0, 0, 1, 0, 1, 0}
};

void copy(){
    for(int i = 0; i < 8; i++)
        for(int j = 0; j < 8; j++)
            adj[i][j] = res[i][j];
}

void square(){
    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 8; j++){
            res[i][j] = 0;
            for(int k = 0; k < 8; k++){
                res[i][j] = (((adj[i][k] % MOD) * (adj[k][j] % MOD)) % MOD + res[i][j] % MOD) % MOD;
            }
        }
    }
    copy();
}

void byone(){
    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 8; j++){
            res[i][j] = 0;
            for(int k = 0; k < 8; k++){
                res[i][j] = (((adj[i][k] % MOD) * (one[k][j] % MOD)) % MOD + res[i][j] % MOD) % MOD;
            }
        }
    }
    copy();
}

void pow(int n){
    if(n == 1) return;
    if(n < 4){
        square();
        if(n == 3) byone();
        return;
    } else {
        pow(n / 2);
        square();
        if(n % 2 != 0) byone();
        return;
    }
}

int main() {
    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 8; j++){
            adj[i][j] = one[i][j];
        }
    }

    cin >> d;
    pow(d);
    cout << adj[0][0] << '\n';
}
