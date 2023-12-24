#include <vector>
#include <iostream>

using namespace std;

typedef pair<int, int> pii;

int n, v;
vector<pii> group;

int solve(){
    if(group.empty()) return n;

    int ret = 987645321, t = 0;
    for(pii& g: group){
        t = (g.first >> 1) + (g.first % 2 != 0);
        t += (g.second - g.first >> 1) + ((g.second - g.first) % 2 != 0);
        ret = min(ret, t);
    }

    return ret + 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> v;
    vector<int> p(n);

    for(int i = 0; i < n; i++) cin >> p[i];

    for(int i = 0; i < n; i++)
        for(int j = i + 1; j < n; j++) 
            if(abs(p[i] - p[j]) >= v)
                group.push_back(pii(i, j));

    cout << solve() << '\n';
}
