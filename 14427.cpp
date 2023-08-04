#include <iostream>

#define MAX 200000
using namespace std;

struct Node {
    int value, idx;
    Node(int value=1000000001, int idx=-1): value(value), idx(idx){}
    bool operator<(const Node& a) const {
        if(this->value < a.value) return true;
        if(this->value == a.value) return this->idx < a.idx;
        return false;
    }
};


Node tree[2 * MAX + 10];
int n, m, a, b, c, nums[MAX + 10];
const Node EPOS = Node();

Node init(int node, int left, int right){
    if(left == right) return tree[node] = Node(nums[left], left);

    int mid = left + right >> 1;
    return tree[node] = min(init(node * 2, left, mid), init(node * 2 + 1, mid + 1, right));
}

Node update(int node, int left, int right, int idx, int value){
    if(left == right) {
        if(left == idx) 
            return tree[node] = Node(value, idx);
        return tree[node];
    }

    int mid = left + right >> 1;
    // 작으면 오른쪽으로 범위 축소
    if(mid < idx)
        return tree[node] = min(tree[node * 2], update(node * 2 + 1, mid + 1, right, idx, value));
    
    else
        return tree[node] = min(update(node * 2, left, mid, idx, value), tree[node * 2 + 1]);
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
        cin >> a;
        if(a == 1) {
            cin >> b >> c;
            update(1, 0, n - 1, b - 1, c);
        }
        else cout << tree[1].idx + 1 << '\n';
    }
}
