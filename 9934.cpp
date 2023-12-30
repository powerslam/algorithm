#include <vector>
#include <iostream>

using namespace std;

// 완전 이진트리가 가정인
// 중위 순회 기반 트리 재구성
vector<int> depth[11];
int k, tree[1024];

void calc(int d, int l, int r){
    if(d == k) return;

    int mid = l + r >> 1;
    depth[d].push_back(tree[mid]);

    calc(d + 1, l, mid - 1);
    calc(d + 1, mid + 1, r);
}

int main() {
    cin >> k;
    for(int i = 0; i < (1 << k) - 1; i++) cin >> tree[i];

    calc(0, 0, (1 << k) - 2);

    for(int i = 0; i < k; i++){
        for(int j: depth[i]) cout << j << ' ';
        cout << '\n';
    }
}
