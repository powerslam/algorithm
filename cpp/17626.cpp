#include <vector>
#include <iostream>
#include <algorithm>

// 제곱수는 223개
#define SQURE 223

using namespace std;

int n;
vector<int> v1, v2;

int solve() {
    if(*lower_bound(v1.begin(), v1.end(), n) == n) return 1;
    if(*lower_bound(v2.begin(), v2.end(), n) == n) return 2;

    for(int i = 0; i < SQURE; i++){
        if(*lower_bound(v2.begin(), v2.end(), n - v1[i]) + v1[i] == n)
            return 3;
    }

    for(int i = 0; i < v2.size(); i++){
        if(*lower_bound(v2.begin(), v2.end(), n - v2[i]) + v2[i] == n)
            return 4;
    }

    return -1;
}

int main() {
    cin >> n;
    
    for(int i = 1; i <= SQURE; i++) v1.push_back(i * i);

    sort(v1.begin(), v1.end());

    for(int i = 0; i < SQURE; i++){
        for(int j = i; j < SQURE; j++){
            v2.push_back(v1[i] + v1[j]);
        }
    }

    sort(v2.begin(), v2.end());
    cout << solve() << '\n';
}
