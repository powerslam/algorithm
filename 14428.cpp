#include <iostream>

#define MAX 200000
using namespace std;

int tree[2 * MAX + 10];
int n, m, a, b, c, nums[MAX + 10];
const int EPOS = 1000000001;

int init(int node, int left, int right){
    if(left == right) return tree[node] = nums[left];

    int mid = left + right >> 1;
    return tree[node] = min(init(node * 2, left, mid), init(node * 2 + 1, mid + 1, right));
}

int update(int node, int left, int right, int idx, int value){
    if(left == right) {
        if(left == idx) 
            return tree[node] = value;
        return tree[node];
    }

    int mid = left + right >> 1;
    // 작으면 오른쪽으로 범위 축소
    if(mid < idx)
        return tree[node] = min(tree[node * 2], update(node * 2 + 1, mid + 1, right, idx, value));
    
    else
        return tree[node] = min(update(node * 2, left, mid, idx, value), tree[node * 2 + 1]);
}

int query(int node, int left, int right, int start, int end){
    if(end < left || right < start) return EPOS;

    if(start <= left && right <= end) return tree[node];
    if(left == right) return tree[node];

    int mid = left + right >> 1;
    return min(query(node * 2, left, mid, start, end), query(node * 2 + 1, mid + 1, right, start, end));
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    init(1, 0, n - 1);

    cin >> m;
    while(m--){
        cin >> a >> b >> c;
        if(a == 1) update(1, 0, n - 1, b - 1, c);
        else cout << query(1, 0, n - 1, b - 1, c - 1) << '\n';
    }
}
