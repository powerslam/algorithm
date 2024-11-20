#include <cmath>
#include <vector>
#include <iostream>

using namespace std;

typedef long long ll;

struct vector2 {
    ll x, y;

    vector2(ll x = 0LL, ll y = 0LL): x(x), y(y){}

    vector2 operator-(const vector2& p) const {
        return vector2(this->x - p.x, this->y - p.y);
    }

    bool operator==(const vector2& p) const {
        return this->x == p.x && this->y == p.y;
    }

    bool operator<(const vector2& p) const {
        if(this->x != p.x) return this->x < p.x;
        return this->y < p.y;
    }

    bool operator<=(const vector2& p) const {
        return !(p < *this);
    }
};

ll ccw(const vector2& p, const vector2& q){
    ll k = p.x * q.y - p.y * q.x;
    if(k > 0) return 1;
    if(k < 0) return -1;
    return 0;
}

ll ccw(const vector2& p, const vector2& q, const vector2& r){
    return ccw(q - p, r - p);
}

typedef pair<vector2, vector2> line;

void swap(vector2& a, vector2& b){
    auto t = a;
    a = b;
    b = t;
}

int solve(line& p, line& q){
    vector2 a = p.first, b = p.second, c = q.first, d = q.second;

    ll v = ccw(a, b, c) * ccw(a, b, d);
    ll w = ccw(c, d, a) * ccw(c, d, b);

    // 평행한 경우
    if(v == 0 && w == 0){
        if(b < a) swap(a, b);
        if(d < c) swap(c, d);

        // 교차 안하는 경우
        if(b < c || d < a) return 0;

        // 시점 == 끝점인 경우
        if(b == c || a == d) return 1;

        if(a == c){
            ll comp = ccw(a, b, d);
            if(comp == 0LL) return 3;
            return 1;
        }

        if(b == d){
            ll comp = ccw(b, a, c);
            if(comp == 0LL)return 3;
            return 1;
        }

        return 3;
    }
    
    if(v <= 0 && w <= 0){
        if(v == 0) return 1;
        if(w == 0) return 1;
        return 2;
    }
    
    return 0;
}

int n;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    vector<line> v(n);

    for(int i = 0; i < n; i++){
        cin >> v[i].first.x >> v[i].first.y >> v[i].second.x >> v[i].second.y;
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << (i == j ? 3 : solve(v[i], v[j]));
        }
        cout << '\n';
    }
}
