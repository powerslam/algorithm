#include <string>
#include <iostream>

using namespace std;

bool visited[1001][1001];
int r, c, board[1001][1001];
int sum = 0;

int main() {
    cin >> r >> c;
    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++)
            cin >> board[i][j];
    
    if(r % 2){
        string h = "D", w1 = "", w2 = "";

        for(int i = 0; i < c - 1; i++)
            w1 += "R", w2 += "L";

        for(int i = 0; i < r - 1; i++){
            if(i % 2 == 0) cout << w1;
            else cout << w2;

            cout << h;
        }

        cout << w1;
    } else if(c % 2) {
        string h = "R", w1 = "", w2 = "";

        for(int i = 0; i < r - 1; i++)
            w1 += "D", w2 += "U";

        for(int i = 0; i < c - 1; i++){
            if(i % 2 == 0) cout << w1;
            else cout << w2;

            cout << h;
        }

        cout << w1;
    } else {
        int my = 0, mx = 1;
        for(int i = 0; i < r; i++)
            for(int j = (i + 1) % 2; j < c; j += 2)
                if((i != r-1 || j != c-1) && board[my][mx] > board[i][j]) 
                    my = i, mx = j;

        string R = "", L = "";
        for(int i = 0; i < c - 1; i++)
            R += 'R', L += 'L';

        // 계산할 때 2칸이 비어야 함!
        // cout << "? : " << my << " " << 2 * (my / 2) << endl;
        for(int i = 0; i < 2 * (my / 2); i += 2){
            cout << R << 'D' << L << 'D';
        }

        // ㄱㄴㄱㄴㄱㄴㄱㄴㄱㄴ 식으로 가야함
        // 0 ~ 4 ==> 제외하기 전
        for(int j = 0; j < mx; j++){
            if(j % 2 == 0) cout << "DR";
            else cout << "UR";
        }

        if(mx == 0) cout << (mx == 0 ? "RD" : "DR");
        else if(mx != c - 1) cout << (mx % 2 == 0 ? "RD" : "RU");
        
        for(int j = mx + 1; j < c - 1; j++){
            if(j % 2 == 0) cout << "RD";
            else cout << "RU";
        }

        for(int i = 2 * (my / 2 + 1); i < r; i++){
            cout << 'D';
            //cout << i << endl;
            if(i % 2 == 0) cout << L;
            else cout << R;
        }
    }

    cout << endl;
}
