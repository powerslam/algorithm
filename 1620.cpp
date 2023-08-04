#include <bits/stdc++.h>
using namespace std;

string t;
vector<string> v1;
map<string, int> v2;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n, m; cin >> n >> m;
    
    for(int i = 0; i < n; i++) {
        cin >> t;
        v1.push_back(t);
        v2[t] = i + 1;
    }

    while(m--){
        cin >> t;
        if(t[0] < 'A') cout << v1[stoi(t) - 1] << '\n';
        else cout << v2[t] << '\n';
    }
}