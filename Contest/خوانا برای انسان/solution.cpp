#include <iostream>

using namespace std;

int main()
{
    int t, m;
    cin >> t;
    for (int i = 0; i < t; i++){
        cin >> m;
        if (m < 1024) cout << to_string(m) << "B" << endl;
        else{
            if ((m / 1024) > 1023) cout << to_string((m / 1024) / 1024) << "MiB" << endl;
            else cout << to_string(m / 1024) << "KiB" << endl;
        }
    }

    return 0;
}