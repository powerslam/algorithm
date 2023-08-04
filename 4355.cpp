#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

ll t, n, ans;
bool visited[1000001];
vector<ll> primes;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    for(int i = 2; i < 1000001; i++){
        if(visited[i]) continue;
        primes.push_back(i);
        for(int j = i; j < 1000001; j += i){
            visited[j] = true;
        }
    }

    while(true){
        cin >> n; 
        if(n == 0) break;

        ans = n;
        if(n == 1){
            cout << 0 << '\n';
            continue;
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
}
