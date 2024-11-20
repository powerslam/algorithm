#include <iostream>

using namespace std;

int n, ans, f, k;
int main() {
    cin >> n >> f;
    for(int i = 0; i < n - 1; i++){
        cin >> k;
        if(k < f) continue;
        if(k == f){
            ans += 1;
            f += 1;
        } else {
            ans += (k - f) / 2 + ((k - f) % 2 != 0 || i == n - 2);
            f += (k - f) / 2 + ((k - f) % 2 != 0 || i == n - 2);
        }
    }    

    cout << ans << '\n';
}
