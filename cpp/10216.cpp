#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct point {
    int x, y, R;
};

bool isInterSection(const point& a, const point& b){
    return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y) <= (a.R + b.R) * (a.R + b.R);
}

vector<point> v;
int t, n, x, y, R;

int find(vector<int>& root, int p){
    if(p == root[p]) return p;
    return root[p] = find(root, root[p]);
}

void onion(vector<int>& root, int p, int q){
    int pp = find(root, p), pq = find(root, q);

    if(pp == pq) return;
    root[pp] = pq;
}

int solve(vector<int>& root){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(isInterSection(v[i], v[j])){
                onion(root, i + 1, j + 1);
            }
        }
    }

    int cnt = 0;
    for(int i = 1; i < n + 1; i++){
        if(i == find(root, i))
            cnt += 1;
    }

    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> t;
    while(t--){
        cin >> n;
        vector<int> root(n + 1);
        for(int i = 0; i < n + 1; i++)
            root[i] = i;

        for(int i = 0; i < n; i++){
            cin >> x >> y >> R;

            point p;
            p.x = x;
            p.y = y;
            p.R = R;

            v.push_back(p);
        }

        cout << solve(root) << '\n';

        vector<point>().swap(v);
    }
}
