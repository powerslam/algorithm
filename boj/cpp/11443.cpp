#include <iostream>

#define MOD 1000000007

using namespace std;
typedef long long ll;

struct matrix {
    ll a, b, c, d;
    matrix(ll a = 0LL, ll b = 0LL, ll c = 0LL, ll d = 0LL): a(a), b(b), c(c), d(d){}

    matrix operator* (const matrix& p){
        return matrix((((this->a % MOD) * (p.a % MOD)) % MOD + ((this->b % MOD) * (p.c % MOD)) % MOD) % MOD,
                    (((this->a % MOD) * (p.b % MOD)) % MOD + ((this->b % MOD) * (p.d % MOD)) % MOD) % MOD,
                    (((this->c % MOD) * (p.a % MOD)) % MOD + ((this->d % MOD) * (p.c % MOD)) % MOD) % MOD,
                    (((this->c % MOD) * (p.b % MOD)) % MOD + ((this->d % MOD) * (p.d % MOD)) % MOD) % MOD);
    }
};

matrix pow(matrix n, ll k){
    if(k == 0) return matrix(1LL, 0LL, 1LL, 0LL);
    if(k == 1) return n;

    matrix tmp = pow(n, k >> 1);
    if(k % 2 == 0) return tmp * tmp;
    return tmp * tmp * n;
}

ll n;
int main(){
    cin >> n; n >>= 1LL;
    cout << pow(matrix(0, 1, 1, 1), 2 * n + 1).b - 1LL << '\n';
}
