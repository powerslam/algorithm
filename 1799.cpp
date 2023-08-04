// 백준알고리즘 1799번 :: 비숍
#include<iostream>
#define max(a,b) a > b ? a : b
using namespace std;
 
int N;
int ans[2];
int chess[11][11];
int l[20];
int r[20];
 
// 놓을 수 있는 비숍의 최대개수를 구하는 함수
// 흑/백, 두 가지 경우로 나누어 계산
 
void tracking(int row, int col, int count, int color)
{
    if (col >= N) {
        row++;
        if(col%2 == 0) col = 1;
        else col = 0;
    }
    if (row >= N) {
        ans[color] = max(ans[color], count);
        return;
    }
 
    if (chess[row][col] && !l[col - row + N - 1] && !r[row + col])
    {
        l[col - row + N - 1] = r[row + col] = 1;
        tracking(row, col+2, count + 1, color);
        l[col - row + N - 1] = r[row + col] = 0;
    }
    tracking(row, col+2, count, color);
}
 
int main(void)
{
    cin >> N;
 
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> chess[i][j];
        }
    }
 
    tracking(0, 0, 0, 0);
    tracking(0, 1, 0, 1);
 
    cout << ans[0] + ans[1];
 
    return 0;
}
