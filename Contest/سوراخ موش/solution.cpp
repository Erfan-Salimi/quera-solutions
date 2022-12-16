#include <bits/stdc++.h>

using namespace std;

int main()
{
    int x1, x2;
    cin >> x1 >> x2;
    if (x1 == x2) cout << "Saal Noo Mobarak!";
    else if (x2 > x1){
        for (int i = 0; i < x2 - x1; i++) cout << 'R';
    }
    else{
        for (int i = 0; i < x1 - x2; i++) cout << 'L';
    }

    return 0;
}
