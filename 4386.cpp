#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

struct Pos {
    double x, y;
    Pos(double x=.0, double y=.0): x(x), y(y) {}
};

Pos pos[101];
int n, uf[101];
double a, b, ans;

struct Edge {
    int a, b;
    double dist;
    Edge(int a, int b): a(a), b(b) {
        this->dist = sqrt((pos[a].x - pos[b].x) * (pos[a].x - pos[b].x) + (pos[a].y - pos[b].y) * (pos[a].y - pos[b].y));
    }
};


vector<Edge> v;

int Find(int p){
    if(p == uf[p]) return p;
    return uf[p] = Find(uf[p]);
}

bool Union(int p, int q){
    p = Find(p);
    q = Find(q);

    uf[p] = q;
    return p != q;
}

int main() {
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> pos[i].x >> pos[i].y;
        uf[i] = i;
    }

    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            v.push_back(Edge(i, j));
        }
    }

    sort(v.begin(), v.end(), [](const Edge& a, const Edge& b){
        return a.dist < b.dist;
    });

    for(int i = 0, cnt = 0; i < v.size() && cnt < n - 1; i++){
        if(Union(v[i].a, v[i].b)){
            ans += v[i].dist;
            cnt += 1;
        }
    }    

    cout << fixed;
    cout.precision(2);
    cout << ans << '\n';
}
