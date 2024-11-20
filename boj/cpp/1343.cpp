#include <iostream>

using namespace std;

const string A = "AAAA", B = "BB";
string s, ans;

int n;
int main() {
    cin >> s; n = s.size();
    
    int cnt = 0;
    for(int i = 0; i < n; i++){
        if(s[i] == '.') {
            if(cnt % 2 != 0) {
                cout << -1 << '\n';
                return 0;
            }

            if(cnt == 2) ans += B;

            ans += ".";
            cnt = 0;
        }
        else {
            cnt += 1;
            if(cnt == 4) {
                ans += A;
                cnt = 0;
            }
        }
    }

    if(cnt == 2) ans += B;
    cout << (cnt % 2 == 0 ? ans : "-1") << '\n';
}
