#include <iostream>

using namespace std;

int main()
{
    int number, summary = 0;
    string s_f;
    cin >> number;
    cin >> s_f;
    for (int i = 0; i < number; i++){
        if (s_f[i] != s_f[i + number]) summary++;
    }
    cout << ((summary == number) ? "YES" : "NO") << endl;

    return 0;
}
