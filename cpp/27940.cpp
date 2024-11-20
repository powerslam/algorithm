#include <iostream>
using namespace std;
int n, m, k, c, a, b, i;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m >> k;
    for(; i < m; i++){
        cin >> a >> b;        
        c += b;
        if(c > k) {
            cout << i + 1 << ' ' << 1 << '\n';
            return 0;
        }
    }

    cout << -1 << '\n';
}
