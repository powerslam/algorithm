#include <queue>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;

int n, num;

int main() {
    cin >> n;
    vector<pii> v(n);
    for(int i = 0; i < n; i++){
        cin >> num >> v[i].first >> v[i].second;
    }

    sort(v.begin(), v.end());

    priority_queue<int> q;
    for(int i = 0; i < n; i++){
        if(q.empty()) q.push(-v[i].second);
        else {
            if(-q.top() <= v[i].first) q.pop();
            q.push(-v[i].second);
        }
        
    }

    cout << q.size() << '\n';
}
