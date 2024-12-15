#include <iostream>

using namespace std;

typedef long long ll;

ll psum[52];
ll combi[52][52];
const ll mod = 1000000007;

ll fast_pow(ll a, ll b){
    ll ret = 1LL;
    ll base = a, expo = b;

    while(expo > 0){
        if(expo % 2LL == 1LL){
            ret = ((ret % mod) * (base % mod)) % mod;
        }

        base = ((base % mod) * (base % mod)) % mod;
        expo >>= 1LL;
    }

    return ret;
}

int n, k;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> k;

    combi[0][0] = 1;
    combi[1][0] = combi[1][1] = 1;
    for(int i = 2; i < 52; i++){
        combi[i][0] = combi[i][i] = 1;
        for(int j = 1; j < i; j++){
            combi[i][j] = ((combi[i - 1][j] % mod) + (combi[i - 1][j - 1] % mod)) % mod;
        }
    }

    psum[0] = n * 1LL;
    for(int i = 2; i < k + 2; i++){
        ll factor = combi[i][1];
        psum[i - 1] = (fast_pow(n + 1, i) % mod - 1LL % mod) % mod;
        
        ll tmp = 0;
        for(int j = 2; j < i + 1; j++){
            tmp = ((combi[i][j] % mod) * (psum[i - j] % mod)) % mod;
            psum[i - 1] = ((psum[i - 1] % mod) - (tmp % mod)) % mod;
        }

        factor = fast_pow(factor, mod - 2);
        psum[i - 1] = ((psum[i - 1] % mod) * (factor % mod)) % mod;
        if(psum[i - 1] < 0) psum[i - 1] += mod;
    }

    cout << psum[k];
}
