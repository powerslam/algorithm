#include <iostream>

#define MOD 10007

using namespace std;

int n, d, mod;
int comb[53][53];

int main(){
    comb[0][0] = comb[1][0] = comb[1][1] = 1;
    for(int i = 2; i < 52; i++){
        comb[i][0] = comb[i][i] = 1;
        for(int j = 1; j < i; j++){
            comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % MOD;
        }
    }

    cin >> n; int ans = 0, sign = 1;
    for(int i = 1; i <= n / 4; i++){
        ans += sign * ((comb[13][i] * comb[52 - i * 4][n - i * 4]) % MOD);
        ans = (ans + MOD) % MOD;
        sign *= -1;
    }

    cout << ans << '\n';
}
