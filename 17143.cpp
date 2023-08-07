#include <iostream>
#include <memory.h>

using namespace std;

struct shark {
    int y, x, s, d, z;
    shark(int y=0, int x=0, int s=0, int d=0, int z=-1): y(y), x(x), s(s), d(d), z(z){}

    void operator=(const shark& k){
        this->y = k.y;
        this->x = k.x;
        this->s = k.s;
        this->d = k.d;
        this->z = k.z;
    }
};

void init(shark& k){
    k.x = 0;
    k.y = 0;
    k.s = 0;
    k.d = 0;
    k.z = -1;
}

int dPos[5][2] = {{0, 0}, {-1, 0}, {1, 0}, {0, 1}, {0, -1}};
int r, c, y, x, m, ans, remain;
int cnt[101][101];
shark s[101][101], ms[101][101];

int fishing(int x){
    for(int y = 1; y <= r; y++){
        if(cnt[y][x] != 0){
            int ret = s[y][x].z;
            s[y][x] = shark();
            cnt[y][x] -= 1;
            return ret;
        }
    }

    return 0;
}

void move(){
    int my, mx;
    for(int y = 1; y <= r; y++){
        for(int x = 1; x <= c; x++){
            if(s[y][x].z == -1) continue;

            my = y + s[y][x].s * dPos[s[y][x].d][0];
            mx = x + s[y][x].s * dPos[s[y][x].d][1];
            
            if(my <= 0) {
                // 상어가 갈 남은 거리
                remain = s[y][x].s - y + 1;

                // 넘은 거라 방향은 1회 무조건 변경
                s[y][x].d = 2;

                // 몫이 짝수 && 나머지 > 0
                if((remain / (r - 1)) % 2 != 0 && remain % (r - 1) > 0)
                    s[y][x].d = 1;
                
                if((remain / (r - 1)) % 2 == 0 && remain % (r - 1) == 0)
                    s[y][x].d = 1;

                int k = remain % (r - 1);
                k = k > 0 ? k : r - 1;

                if(s[y][x].d == 1) my = r - k;
                else my = 1 + k;
            }
            else if(mx <= 0) {
                // 상어가 갈 남은 거리
                remain = s[y][x].s - x + 1;

                // 넘은 거라 방향은 1회 무조건 변경
                s[y][x].d = 3;

                // 몫이 짝수 && 나머지 > 0
                if((remain / (c - 1)) % 2 != 0 && remain % (c - 1) > 0)
                    s[y][x].d = 4;
                
                // 몫이 짝수 && 나머지 > 0
                if((remain / (c - 1)) % 2 == 0 && remain % (c - 1) == 0)
                    s[y][x].d = 4;

                int k = remain % (c - 1);
                k = k > 0 ? k : c - 1;

                if(s[y][x].d == 4) mx = c - k;
                else mx = 1 + k;
            }
            else if(my > r) {
                // 상어가 갈 남은 거리
                remain = s[y][x].s - r + y;

                // 넘은 거라 방향은 1회 무조건 변경
                s[y][x].d = 1;

                // 몫이 짝수 && 나머지 > 0 
                if((remain / (r - 1)) % 2 != 0 && remain % (r - 1) > 0)
                    s[y][x].d = 2;

                if((remain / (r - 1)) % 2 == 0 && remain % (r - 1) == 0)
                    s[y][x].d = 2;
                
                int k = remain % (r - 1);
                k = k > 0 ? k : r - 1;

                if(s[y][x].d == 1) my = r - k;
                else my = 1 + k;
            }
            else if(mx > c) {
                // 상어가 갈 남은 거리
                remain = s[y][x].s - c + x;

                // 넘은 거라 방향은 1회 무조건 변경
                s[y][x].d = 4;

                // 몫이 짝수 && 나머지 > 0
                if((remain / (c - 1)) % 2 != 0 && remain % (c - 1) > 0)
                    s[y][x].d = 3;

                // 몫이 짝수 && 나머지 > 0
                if((remain / (c - 1)) % 2 == 0 && remain % (c - 1) == 0)
                    s[y][x].d = 3;

                int k = remain % (c - 1);
                k = k > 0 ? k : c - 1;

                if(s[y][x].d == 4) mx = c - k;
                else mx = 1 + k;
            }

            s[y][x].y = my;
            s[y][x].x = mx;

            // 이미 이곳에 상어가 있는 경우
            if(ms[my][mx].z != -1){
                // 있던 상어보다 지금 상어가 더 큰 경우
                if(ms[my][mx].z < s[y][x].z){
                    ms[my][mx] = s[y][x];
                    ms[my][mx].y = my;
                    ms[my][mx].x = mx;

                    cnt[y][x] -= 1;
                } 
                
                // 지금 상어가 이전 상어보다 작은 경우
                else {
                    s[y][x] = shark();
                    cnt[y][x] -= 1;
                }
            } 
            
            // 방문한 적 없는 곳인 경우
            else {
                // 방문 표시하고
                ms[my][mx] = s[y][x];
                init(s[y][x]);

                cnt[y][x] -= 1;
                cnt[my][mx] += 1;
            }
        }
    }

    for(int i = 1; i <= r; i++){
        for(int j = 1; j <= c; j++){
            s[i][j] = ms[i][j];
            init(ms[i][j]);
        }
    }
}

void print(){
    for(int i = 1; i <= r; i++){
        for(int j = 1; j <= c; j++){
            cout << cnt[i][j] << ' ';
        }
        cout << '\n';
    }
    cout << '\n';
}

int main(){
    cin >> r >> c >> m;

    for(int i = 0; i < m; i++){
        cin >> y >> x;
        cin >> s[y][x].s >> s[y][x].d >> s[y][x].z;
        s[y][x].y = y;
        s[y][x].x = x;
        cnt[y][x] += 1;
    }

    for(int i = 1; i < c; i++){
        ans += fishing(i);
        move();
    }

    ans += fishing(c);
    cout << ans << '\n';
}
