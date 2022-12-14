#include <iostream>

using namespace std;

int main()
{
    char hands[4];
    for (int i = 0; i < 4; i++) cin >> hands[i];
    cout << ((hands[0] == hands[1] || hands[0] == hands[3] || hands[1] == hands[2] || hands[2] == hands[3]) ? "YES" : "NO");
    
    return 0;
}
