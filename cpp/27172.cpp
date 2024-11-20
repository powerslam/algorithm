#include <iostream>

using namespace std;

bool exist[1000001];
int n, player[100001], cards[1000001];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> player[i];
        exist[player[i]] = true;
    }

    for(int i = 0; i < n; i++){
        for(int j = 1; j * j <= player[i]; j++){
            if(exist[j] && player[i] % j == 0){
                cards[player[i]] -= 1;
                cards[j] += 1;
            }

            if(player[i] / j != j && exist[player[i] / j] && player[i] % (player[i] / j) == 0){
                cards[player[i]] -= 1;
                cards[player[i] / j] += 1;
            }
        }
    }

    for(int i = 0; i < n; i++) cout << cards[player[i]] << ' ';
    cout << endl; 
}
