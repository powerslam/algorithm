// small(12033), large(12034) 코드 동일

#include <queue>
#include <iostream>

using namespace std;

int t, n, v;
queue<int> q;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> t;
    for(int i = 0; i < t; i++){
        cout << "Case #" << i + 1 << ": ";
        cin >> n; n <<= 1;

        while(n--){
            cin >> v;
            if(!q.empty() && q.front() == v) q.pop();
            else {
                q.push(v / 3 << 2);
                cout << v << ' ';
            }
        }

        cout << '\n';
    }
}
