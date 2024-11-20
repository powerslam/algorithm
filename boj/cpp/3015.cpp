#include <map>
#include <iostream>

using namespace std;

typedef long long ll;

int n, top = -1;
map<ll, ll> m;
ll tall, ans, st[51];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    while(n--){
        cin >> tall;
        m[tall] += 1LL;

        if(top == -1) st[++top] = tall;        
        else {
            // top 보다 입력값이 큰 경우
            while(top != -1 && st[top] < tall){
                ans += m[st[top]];
                m[st[top--]] = 0LL;
            }

            if(top != -1){
                if(st[top] > tall){
                    ans += 1LL;
                } else {
                    ans += m[st[top]] - 1LL;
                    if(top > 0) ans += 1LL;
                }
            }

            if(top == -1 || st[top] != tall) 
                st[++top] = tall;
        }
    }

    cout << ans << '\n';
}
