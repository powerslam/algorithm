#include <string>
#include <iostream>

using namespace std;

string s;
int m, k, t;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> m;
    while(m--){
        cin >> s;
        if(s[1] == 'l') k = (1 << 21) - 1;
        else if(s[0] == 'e') k = 0;
        else {
            cin >> t;
            if(s[0] == 'r') k &= ~(1 << t);
            else if(s[0] == 'c') cout << ((k & (1 << t)) == (1 << t)) << '\n';
            else if(s[0] == 't') k ^= (1 << t);
            else if(s[1] == 'd') k |= 1 << t; 
        }
    }
}
