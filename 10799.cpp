#include <vector>
#include <string>
#include <iostream>

using namespace std;

string s;
vector<int> v;
int cnt[100001], ans;
int main() {
    cin >> s;

    for(int i = 0; i < s.size(); i++){
        if(s[i] == '(')
            v.push_back(i);

        else {
            if(i - v.back() + 1 < 3) cnt[i] += 1;
            else {
                ans += cnt[i] - cnt[v.back()] + 1;
            }

            v.pop_back();
        }

        cnt[i + 1] = cnt[i];
    }

    cout << ans << '\n';
}
