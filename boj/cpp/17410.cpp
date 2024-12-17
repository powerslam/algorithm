#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;

int sn = 1800;

vector<int> nums(100001);
vector<vector<pii>> bucket(sn);

int n, tmp, m, a, b, c, o;

bool comp(const pii& a, const pii& b){
    return a.first < b.first;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;

    for(int i = 0; i < n; i++){
        cin >> nums[i];
        bucket[(int) i / sn].push_back(pii(nums[i], i));
    }

    for(int i = 0; i < sn; i++){
        sort(bucket[i].begin(), bucket[i].end());
    }
    
    cin >> m;
    while(m--){
        cin >> o;
        if(o == 1){
            cin >> a >> b;
            
            a -= 1;
            nums[a] = b;

            auto& _bucket = bucket[(int) a / sn];
            int idx = 0, len = _bucket.size();
            for(; idx < len; idx++){
                if(_bucket[idx].second == a){
                    _bucket[idx].first = b;
                    break;
                }
            }

            while(idx < len - 1 && _bucket[idx].first > _bucket[idx + 1].first){
                swap(_bucket[idx], _bucket[idx + 1]);
                idx += 1;
            }

            while(idx > 0 && _bucket[idx].first < _bucket[idx - 1].first){
                swap(_bucket[idx], _bucket[idx - 1]);
                idx -= 1;
            }
        }

        else {
            cin >> a >> b >> c;
            a -= 1, b -= 1;

            int ans = 0;
            while(a % sn != 0 && a <= b){
                ans += (nums[a] > c) ? 1 : 0;
                a += 1;
            }

            while((b + 1) % sn != 0 && a <= b){
                ans += (nums[b] > c) ? 1 : 0;
                b -= 1;
            }

            while(a <= b){
                const pii& target = pii(c + 1, 0);
                int find = lower_bound(bucket[(int) a / sn].begin(), bucket[(int) a / sn].end(), target, comp) - bucket[(int) a / sn].begin();
                ans += bucket[(int) a / sn].size() - find;
                a += sn;
            }

            cout << ans << '\n';
        }
    }
}
