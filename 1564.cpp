#include <stdio.h>
#define MOD 100000

int n, t, cnt2, cnt5, ans = 1;
int ten[10] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000};

int pow(int a, int b){
    if(b == 0) return 1;

    int tmp = pow(a, b >> 1);
    tmp = (tmp % MOD) * (tmp % MOD) % MOD;
    
    if(b % 2 == 0) return tmp;
    return (tmp % MOD) * (a % MOD) % MOD;
}

int main(){
    scanf("%d", &n);
    for(int i = 1; i <= n; i++){
        int k = i;
        while(k % 2 == 0){
            cnt2++;
            k >>= 1;
        }

        while(k % 5 == 0){
            cnt5++;
            k /= 5;
        }

        if(cnt2 > 0 && cnt5 > 0){
            t = cnt2 < cnt5 ? cnt2 : cnt5;
            cnt2 -= t;
            cnt5 -= t;
        }

        ans = (ans % MOD) * (k % MOD) % MOD;
    }

    if(cnt2 > 0 && cnt5 > 0){
        t = cnt2 < cnt5 ? cnt2 : cnt5;
        cnt2 -= t;
        cnt5 -= t;
    }

    ans = (ans % MOD) * (pow(2, cnt2) % MOD) % MOD;
    ans = (ans % MOD) * (pow(5, cnt5) % MOD) % MOD;

    printf("%05d\n", ans % MOD);
}
