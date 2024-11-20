#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
int N;
int x, y;
int field[100][100];
int visited[100][100];
int house[1000];
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };
queue<pair<int, int>>q;

void BFS() {
	int count = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
            if(!field[i][j]) continue;

            q.push(make_pair(j, i));
            field[i][j] = 0;
            visited[i][j] = true;
            house[count]++;

            while (!q.empty()) {
                x = q.front().first;
                y = q.front().second;
                q.pop();

                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if(nx < 0 || nx >= N || ny < 0 || ny > N) continue;
                    if(visited[ny][nx]) continue;
                    
                    field[ny][nx] = 0;
                    visited[ny][nx] = true;
                    q.push(make_pair(nx, ny));
                    house[count]++;
				}
				count++;
			}
		}
	}
	sort(house, house + count);
	cout << count << "\n";
	for (int i = 0; i < count; i++) {
		cout << house[i] << "\n";
	}
}

int main() {
	ios_base::sync_with_stdio(false);cin.tie(NULL); cout.tie(NULL);
	cin >> N;
	char a;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> a;
			if (a == '0') {
				field[i][j] = 0;
				visited[i][j] = true;
			}
			else {
				field[i][j] = 1;
			}
		}
	}
	BFS();
	return 0;
}