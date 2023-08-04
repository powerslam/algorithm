#include <cmath>
#include <iostream>

#define EPSILON 1e-10

using namespace std;

struct vector2{
    double x, y;
    vector2(double x = 0, double y = 0): x(x), y(y) {}

    double cross(const vector2& v) const {
        return this->x * v.y - this->y * v.x;
    }

    bool operator< (const vector2& v){
        return (this-> x != v.x) ? this->x < v.x : this->y < v.y;
    }
};

double cross(vector2 a, vector2 b, vector2 c){
    return vector2(b.x - a.x, b.y - a.y).cross(vector2(c.x - a.x, c.y - a.y));
}

void swap(vector2& a, vector2& b){
    auto t = a;
    a = b;
    b = t;
}

vector2 a, b, c, d;
int main() {
    cout << fixed;
    cout.precision(10);

    cin >> a.x >> a.y >> b.x >> b.y;
    cin >> c.x >> c.y >> d.x >> d.y;
    
    double comp1 = cross(a, b, c) * cross(a, b, d);
    double comp2 = cross(c, d, a) * cross(c, d, b);
    
    double p = (b.y - a.y) / (b.x - a.x);
    double q = (d.y - c.y) / (d.x - c.x);

    if(comp1 == 0 && comp2 == 0){    
        if(b < a) swap(a, b);
        if(d < c) swap(c, d);

        if(b < c || d < a) cout << "0\n";
        else {
            cout << "1\n";
            
            if(b.x == c.x && b.y == c.y)
                cout << b.x << ' ' << b.y << '\n';

            else if(d.x == a.x && d.y == a.y)
                cout << a.x << ' ' << a.y << '\n';

            else if(fabs(p - q) >= EPSILON){
                if(b.x == d.x && b.y == d.y)
                    cout << b.x << ' ' << b.y << '\n';

                else if(c.x == a.x && c.y == a.y)
                    cout << a.x << ' ' << a.y << '\n';
            }
        }
    }
    else if(comp1 <= 0 && comp2 <= 0){
        cout << "1\n";
        if(fabs(b.x - a.x) < EPSILON){
            cout << a.x << ' ' << q * (a.x - c.x) + c.y << '\n';
        } else if(fabs(d.x - c.x) < EPSILON){
            cout << c.x << ' ' << p * (c.x - a.x) + a.y << '\n';
        } else {
            double x = (a.x * p - c.x * q + c.y - a.y) / (p - q);
            cout << x << ' ' << p * (x - a.x) + a.y << '\n';
        }
    }
    else cout << "0\n";
}
