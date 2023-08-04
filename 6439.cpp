#include <iostream>

using namespace std;

struct vector2 {
    int x, y;
    vector2(int x = 0, int y = 0): x(x), y(y){}

    vector2 operator-(const vector2& v) const {
        return vector2(this->x - v.x, this->y - v.y);
    }

    bool operator< (const vector2& v) const {
        return this->x != v.x ? this->x < v.x : this->y < v.y;
    }
};

int cross(const vector2& a, const vector2& b){
    return a.x * b.y - a.y * b.x;
}

int cross(const vector2& a, const vector2& b, const vector2& c){
    return cross(b - a, c - a);
}

void swap(vector2& a, vector2& b){
    auto t = a;
    a = b;
    b = t;
}

bool cross(vector2& a, vector2& b, vector2& c, vector2& d){
    int comp1 = cross(a, b, c) * cross(a, b, d);
    int comp2 = cross(c, d, a) * cross(c, d, b);

    if(comp1 == 0 && comp2 == 0) {
        if(b < a) swap(a, b);
        if(d < c) swap(c, d);

        return !(b < c || d < a);
    }

    return comp1 <= 0 && comp2 <= 0;
}

int c, t;
vector2 a, b, lt, lb, rt, rb;

char solve() {
    if(cross(a, b, lt, lb)) return 'T';
    if(cross(a, b, lt, rt)) return 'T';
    if(cross(a, b, rt, rb)) return 'T';
    if(cross(a, b, lb, rb)) return 'T';

    // 사각형 범위 안에 선분 들어가나 비교
    if(lt.x <= a.x && a.x <= rb.x && rb.y <= a.y && a.y <= lt.y)
        if(lt.x <= b.x && b.x <= rb.x && rb.y <= b.y && b.y <= lt.y)
            return 'T';

    return 'F';
}

int main() {
    cin >> c;
    while(c--){
        cin >> a.x >> a.y >> b.x >> b.y >> lt.x >> lt.y >> rb.x >> rb.y;

        if(rb.x < lt.x){
            t = rb.x;
            rb.x = lt.x;
            lt.x = t;
        }

        if(lt.y < rb.y){
            t = rb.y;
            rb.y = lt.y;
            lt.y = t;    
        }

        lb.x = lt.x, lb.y = rb.y;
        rt.x = rb.x, rt.y = lt.y;
        
        cout << solve() << '\n';
    }
}
