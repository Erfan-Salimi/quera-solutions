#include <iostream>

using namespace std;

int main()
{
    int number;
    cin >> number;
    string result = "q";
    for (int i = 0; i < number - 1; i++) result += "u";
    cout << result << endl;

    return 0;
}
