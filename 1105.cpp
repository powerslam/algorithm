#include <iostream>

using namespace std;

string l, r;
int solve() {
    if(l.size() != r.size()) return 0;
    if(l.find('8') == string::npos) return 0;
    if(r.find('8') == string::npos) return 0;

    int ans = 0, n = l.size();
    for(int i = 0; i < n; i++){
        if(l[i] == r[i]){
            if(l[i] == '8') ans++;
        } else return ans;
    }

    return ans;
}

int main(){
    cin >> l >> r;
    cout << solve() << '\n';
}
