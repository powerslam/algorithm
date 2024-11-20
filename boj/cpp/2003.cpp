#include <iostream>

using namespace std;

int ans, n, m, arr[10001], sum[10010];
int main(){
    cin >> n >> m >> arr[0];
    sum[1] = arr[0];
    
    for(int i = 1; i < n; i++){
        cin >> arr[i];
        sum[i + 1] = sum[i] + arr[i];
    }

    int s = 0, e = 1;
    while(e < n + 1){
        int t = sum[e] - sum[s];
        if(t < m) e += 1;
        else {
            if(t == m) ans += 1;
            s += 1;
        }
    }

    cout << ans << endl;
}