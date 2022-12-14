#include <bits/stdc++.h>

using namespace std;

int main()
{
    string text;
    int summary = 0;
    cin >> text;
    for (char i: text){
        if (i == 'a' || i == 'i' || i == 'u' || i == 'o' || i == 'e') summary++;
    }
    cout << pow(2, summary);

    return 0;
}
