#include <iostream>

using namespace std;

int main()
{
    string text[2];
    for (int i = 0; i < 2; i++) cin >> text[i];
    cout << ((text[0][0] == text[1][text[1].size() - 1]) ? "YES" : "NO");

    return 0;
}
