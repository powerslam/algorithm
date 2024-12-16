#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;

int maxN = 75000;

vector<pii> pts;
ll ans, t, n, x, y;
vector<ll> tree(maxN * 4);

void update(int node, int nl, int nr, int k){
    if(nl == nr){
        tree[node] += 1LL;
        return;
    }

    int mid = nl + nr >> 1;
    if(k <= mid){
        update(node * 2, nl, mid, k);
    }

    else{
        update(node * 2 + 1, mid + 1, nr, k);
    }

    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

ll query(int node, int nl, int nr, int sl, int sr){
    if(sr < nl || nr < sl){
        return 0LL;
    }

    if(sl <= nl && nr <= sr){
        return tree[node];
    }

    int mid = nl + nr >> 1;
    return query(node * 2, nl, mid, sl, sr) + query(node * 2 + 1, mid + 1, nr, sl, sr);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> t;
    while(t--){
        ans = 0LL;
        vector<ll>(maxN * 4).swap(tree);
        vector<pii>().swap(pts);

        cin >> n;
        for(int i = 0; i < n; i++){
            cin >> x >> y;
            pts.push_back(pii(y, x));
        }

        sort(pts.begin(), pts.end());
        
        int rank = -1, prev = 1000000001;
        for(int i = 0; i < n; i++){
            if(prev != pts[i].first) rank += 1;
            prev = pts[i].first;

            pts[i].first = pts[i].second;
            pts[i].second = -rank;
        }

        sort(pts.begin(), pts.end());

        for(int i = 0; i < n; i++){
            pts[i].second *= -1;
            ans += query(1, 0, maxN - 1, pts[i].second, maxN - 1);            
            update(1, 0, maxN - 1, pts[i].second);
        }

        cout << ans << '\n';
    }
}
