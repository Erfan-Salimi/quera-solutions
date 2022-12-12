#include<bits/stdc++.h>
using namespace std;
int main()
{
    string number;
    cin >> number;
        
    for (int i = 0; i < number.size(); i++) {
        int a = number[i] - '0';
        cout << a << ": ";
        
        for (int j = 0; j < a; j++) {
            cout << a;
        }
        cout << endl;
    }
}
