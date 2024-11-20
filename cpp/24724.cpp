#include <iostream>

using namespace std;

int t, n, a, b;
int main() {
    cin >> t;
    for(int i = 0; i < t; i++){
        cout << "Material Management " << i + 1 << endl;
        cin >> n >> a >> b;
        while(n--) cin >> a >> b;
        cout << "Classification ---- End!\n";
    }
}
