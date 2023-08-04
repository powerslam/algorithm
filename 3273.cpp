#include <iostream>
#include <algorithm>

using namespace std;

int n, nums[100001], s, e, x, ans;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> nums[i];
    cin >> x;

    sort(nums, nums + n);

    s = 0, e = n - 1;
    while(s < e){
        if(nums[s] + nums[e] < x){
            s += 1;
        } else if(nums[s] + nums[e] == x){
            e -= 1;
            ans += 1;
        } else e -= 1;
    }

    cout << ans << '\n';
}
