#include <iostream>

using namespace std;

int main() {
    string s; cin >> s;

    char prev = s[0];
    int zc = 0, oc = 0;
    for(int i = 1; i < s.size(); i++){
        if(prev != s[i])
            s[i] == '0' ? oc += 1 : zc += 1;

        prev = s[i];
    }

    if(s[s.size() - 1] == '0') zc += 1;
    else oc += 1;

    cout << min(oc, zc) << '\n';
}
