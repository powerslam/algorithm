#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;

int n, q, l, r;
vector<int> lef[1000001], rig[1000001];

int solve() {
    cin >> l >> r;
    if(lef[l].empty() || rig[r].empty()) return -1;
    if(*lef[l].rbegin() < r) return -1;
    if(*rig[r].begin() > l) return -1;

    // r이 있으면 바로 1 리턴
    bool f = binary_search(lef[l].begin(), lef[l].end(), r);
    if(f) return 1;
    return 2;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> l >> r;
        lef[l].push_back(r);
        rig[r].push_back(l);
    }

    cin >> q;
    for(int i = 0; i < 1000001; i++){
        sort(lef[i].begin(), lef[i].end());
        sort(rig[i].begin(), rig[i].end());
    }

    while(q--) cout << solve() << '\n';
}
