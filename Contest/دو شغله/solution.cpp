#include <iostream>

using namespace std;

int main()
{
    string text;
    cin >> text;
    if (text == "shanbe" || text == "doshanbe" || text == "chaharshanbe") cout << "perspolis" << endl;
    else if(text != "jome") cout << "bahman" << endl;
    else cout << "tatil" << endl;

    return 0;
}
