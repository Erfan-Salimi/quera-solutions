#include<iostream>

using namespace std;

int main(){
    int n, a;
    cin >> n;

    for (int i = 0; i < n; i++){
        cin >> a;
        if (a > 15)
            cout << "cooler" << endl;
        else
            cout << "heater" << endl;
    }

    return 0;
}
