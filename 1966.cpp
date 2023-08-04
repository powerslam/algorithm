#include <deque>
#include <queue>
#include <iostream>

using namespace std;

typedef priority_queue<int, vector<int>> heap;

deque<int> arr; heap q;
int p, t, n, m, k;
int main() {
    cin >> t;
    while(t--){
        cin >> n >> m;

        for(int i = 0; i < n; i++){
            cin >> k;
            arr.push_back(k);
            q.push(k);
        }

        p = arr[m];
        int ans = 1;
        while(!arr.empty()){
            if(q.top() > arr.front()){
                arr.push_back(arr.front());
                arr.pop_front();
                if(m == 0) m = arr.size() - 1;
                else m -= 1;
            } else {
                if(m == 0){ 
                    cout << ans << endl;
                    break;
                }

                arr.pop_front();
                q.pop();

                m -= 1;
                ans += 1;
            }
        }

        deque<int>().swap(arr);
        heap().swap(q);
    }
}
