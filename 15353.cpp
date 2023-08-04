#include <string>
#include <vector>
#include <iostream>
using namespace std;

string A, B;

void swap(string& a, string& b){
    auto c = a;
    a = b;
    b = c;
}

int main(){
    cin >> A >> B;

    if(A.length() < B.length()) swap(A, B);
    vector<char> a(A.rbegin(), A.rend()), b(B.rbegin(), B.rend());
    
    int la = a.size(), lb = b.size();
// 9번 20번 21번
    int carry = 0;
    for(int i = 0; i < lb; i++){
        int now = carry + (a[i] - '0') + (b[i] - '0');

        carry = now / 10;
        now %= 10;

        a[i] = now + '0';
    }

    if(a.size() > b.size()){
        for(int i = lb; i < la; i++){
            int now = carry + (a[i] - '0');

            carry = now / 10;
            now %= 10;

            a[i] = now + '0';
        }
    }
    
    if(carry != 0) cout << carry;
    for(auto iter = a.rbegin(); iter != a.rend(); iter++){
        cout << *iter;
    }
}
