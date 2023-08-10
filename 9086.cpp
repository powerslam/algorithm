#include <iostream>

using namespace std;

int t;
string s;
int main() {
    cin >> t;
    while(t--){
        cin >> s;
        cout << *s.begin() << *s.rbegin() << '\n';
    }
}
