#include <vector>
#include <iostream>

#define MAX 5000000

using namespace std;

int n, k;
int spf[MAX + 1];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    for(int i = 2; i < MAX + 1; i++){
        if(spf[i] != 0) continue;
        for(int j = i; j < MAX + 1; j += i){
            if(spf[j] == 0) spf[j] = i;
        }
    }

    cin >> n;
    while(n--){
        cin >> k;
        while(k != 1){
            cout << spf[k] << ' ';
            k /= spf[k];
        }
        cout << '\n';
    }
}
