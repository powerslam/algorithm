#include <iostream>

using namespace std;

char x;
string s;
int n, m, o, str[10001];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> s;
        for(char c: s)
            str[i] |= 1 << (c - 'a');
    }

    int know = (1 << 27) - 1;
    while(m--){
        int cnt = 0;
        cin >> o >> x;
        know ^= 1 << (x - 'a');

        for(int i = 0; i < n; i++)
            if((str[i] & know) == str[i])
                cnt++;
    
        cout << cnt << '\n';
    }
}
