#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

ll t, n, ans;
bool visited[1000001];
vector<ll> primes;

int main() {
    cin >> n; ans = n;
    for(int i = 2; i < 1000001; i++){
        if(visited[i]) continue;
        primes.push_back(i);
        for(int j = i; j < 1000001; j += i){
            visited[j] = true;
        }
    }
    
    for(ll p: primes){
        if(n % p == 0){
            ans /= p;
            ans *= (p - 1LL);
        }
        
        while(n % p == 0) n /= p;
    }
    
    if(n != 1LL) ans /= n, ans *= (n - 1LL);
    cout << ans << '\n';
}
