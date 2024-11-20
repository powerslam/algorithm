#include <vector>
#include <iostream>

using namespace std;

typedef long long ll;

struct Vector2 {
    ll x, y;
    Vector2(ll x = 0LL, ll y = 0LL): x(x), y(y){}

    ll cross(Vector2 v){
        return this->x * v.y - this->y * v.x;
    }

    bool operator< (Vector2 v){
        if(this->x != v.x)
            return this->x < v.x;
        return this->y < v.y;
    }
};

typedef pair<Vector2, Vector2> Line;

Vector2 a, b;
int n, ans, uf[3030], sz[3030];

ll cross(Vector2 a, Vector2 b){
    return a.cross(b);
}

ll cross(Vector2 a, Vector2 b, Vector2 c){
    return cross(Vector2(b.x - a.x, b.y - a.y), Vector2(c.x - a.x, c.y - a.y));
}

int Find(int p){
    if(uf[p] == p) return p;
    return uf[p] = Find(uf[p]);
}

int Union(int p, int q){
    p = Find(p);
    q = Find(q);

    if(p == q) return false;
    p < q ? uf[p] = q, sz[q] += sz[p] : uf[q] = p, sz[p] += sz[q];
    return true;
}

void swap(Vector2& a, Vector2& b){
    auto t = a;
    a = b;
    b = t;
}

int main() {
    cin >> n; ans = n;
    vector<Line> v;
    for(int i = 0; i < n; i++){
        cin >> a.x >> a.y >> b.x >> b.y;
        if(b < a) swap(a, b);

        v.push_back(Line(a, b));
        uf[i] = i;
        sz[i] = 1;
    }

    for(int i = 0; i < n; i++){
        // v[i]: a, b
        for(int j = i + 1; j < n; j++){
            // v[j]: c, d
            ll comp1 = cross(v[i].first, v[i].second, v[j].first) * cross(v[i].first, v[i].second, v[j].second);
            ll comp2 = cross(v[j].first, v[j].second, v[i].first) * cross(v[j].first, v[j].second, v[i].second);

            if(comp1 == 0LL && comp2 == 0LL){
                if(v[i].second < v[j].first || v[j].second < v[i].first)
                    continue;

                if(Union(i, j)) ans -= 1;
            } else if(comp1 <= 0LL && comp2 <= 0LL){
                if(Union(i, j)) ans -= 1;
            }
        }
    }

    cout << ans << '\n';

    ans = 0;
    for(int i = 0; i < n; i++){
        if(i != Find(i)) continue;
        ans = max(ans, sz[i]);
    }

    cout << ans << '\n';
}
