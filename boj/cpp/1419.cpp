#include <iostream>

using namespace std;

int l, r, k, t;
int main() {
    cin >> l >> r >> k;
    
    if(k & 1) {
        t = k + 1 >> 1;
        l = (l + k - 1) / k;
        r = r / k;

        cout << (t > r ? 0 : r - max(l, t) + 1) << '\n';
    } else {
        t = k + 1;
        l = (l + k / 2 - 1) / (k / 2);
        r = r / (k / 2);

        cout << (t > r ? 0 : r - max(l, t) + 1 - (k == 4 && l <= 6 && 6 <= r));
    }
}
