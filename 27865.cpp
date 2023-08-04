#include <ctime>
#include <cstdlib>
#include <iostream>

using namespace std;

char ret;
int n;
int main() {
    cin >> n;
    for(int i = 0; i < 20001 && ret != 'Y'; i++){
        cout << "? 1\n" << flush;
        cin >> ret;
    }

    cout << "! 1\n" << flush;
}
