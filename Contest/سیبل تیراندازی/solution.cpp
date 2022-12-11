#include <iostream>

using namespace std;

int main()
{
    int number;
    cin >> number;
    if (number == 0) cout << "out" << endl;
    else if(number < 7) cout << "white" << endl;
    else cout << "black" << endl;

    return 0;
}
