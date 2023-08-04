#include <cstdio>

using namespace std;

int a;
int main() {
    while(scanf("%d", &a) != -1){
        printf(a % 6 == 0 ? "Y" : "N");
        printf("\n");
    }
}
